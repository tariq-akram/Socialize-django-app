# travelapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/user/', views.user_login_view, name='user_login'),
    path('login/admin/', views.admin_login_view, name='admin_login'),
    path('logout/', views.user_logout_view, name='logout'),
    path('change-password/', views.change_password_view, name='change_password'),
    path('admin_dashboard/', views.admin_dashboard_view, name='admin_dashboard'),
    path('signup/', views.user_signup_view, name='signup'),
    path('user/dashboard/', views.user_dashboard, name='user_dashboard'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('admin_add_post/', views.add_post, name='add_post'),
    path('admin_view_comments/', views.view_comments, name='view_comments'),
]
