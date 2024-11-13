# travelapp/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.contrib import messages
from .forms import UserLoginForm, AdminLoginForm, UserSignupForm
from django.contrib.auth.models import User
from .models import Post, Comment

def home_view(request):
    return render(request, "body.html")

def is_admin(user):
    return user.is_staff

def is_normal_user(user):
    return not user.is_staff

def user_login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if not user.is_staff:
                login(request, user)
                messages.success(request, "Login successful!")
                return redirect('user_dashboard')
            else:
                messages.error(request, "Invalid credentials for normal user.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = UserLoginForm()
    return render(request, "user_login.html", {"form": form})

def admin_login_view(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect('admin_dashboard')
        else:
            return redirect('home')
    if request.method == "POST":
        form = AdminLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_staff:
                login(request, user)
                messages.success(request, "Admin login successful!")
                return redirect('admin_dashboard')
            else:
                messages.error(request, "You are not authorized as admin.")
        else:
            messages.error(request, "Invalid admin credentials.")
    else:
        form = AdminLoginForm()
    return render(request, "admin_login.html", {"form": form})

def user_logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('home')

@login_required
def change_password_view(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Keeps user logged in
            messages.success(request, "Your password was successfully updated!")
            return redirect('home')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = PasswordChangeForm(request.user)
    return render(request, "change_password.html", {"form": form})

# Admin Dashboard View
@login_required
@user_passes_test(lambda u: u.is_staff)
def admin_dashboard_view(request):
    users = User.objects.all()
    posts = Post.objects.all()
    comments = Comment.objects.all()
    context = {
        'users': users,
        'posts': posts,
        'comments': comments
    }
    return render(request, "admin_dashboard.html", context)



def user_signup_view(request):
    if request.method == "POST":
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = False  # Ensure user is not staff
            user.save()
            messages.success(request, "Account created successfully! Please log in.")
            return redirect('user_login')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = UserSignupForm()
    return render(request, "signup.html", {"form": form})


@login_required
@user_passes_test(is_normal_user)
def user_dashboard(request):
    posts = Post.objects.all()
    return render(request, 'user_dashboard.html', {'posts': posts})

@login_required
@user_passes_test(is_admin)
def add_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Post.objects.create(title=title, content=content)
        return redirect('admin_dashboard')
    return render(request, 'add_post.html')

@login_required
@user_passes_test(is_admin)
def view_comments(request):
    comments = Comment.objects.select_related('post', 'user').all()
    return render(request, 'view_comments.html', {'comments': comments})


@login_required
@user_passes_test(is_normal_user)
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all()

    if request.method == 'POST':
        content = request.POST['content']
        Comment.objects.create(user=request.user, post=post, content=content)
        return redirect('post_detail', post_id=post.id)

    return render(request, 'post_details.html', {'post': post, 'comments': comments})