# Socialize - Python Web Application

## Overview

socialize is a Python web application built using Django, designed to manage posts and comments with separate functionalities for Admin and Normal Users.

## Features

### Normal Users:
- **Login**: Secure login functionality.
- **Change Password**: Update account password.
- **View Posts**: Access and read the latest posts.
- **Add Comments**: Engage by adding comments to posts.

### Admin Users:
- **Login**: Secure admin login.
- **View All Users**: Access a dashboard listing all registered users.
- **Add Posts**: Create new posts for users to view.
- **View Comments**: Monitor and manage comments added to posts.

## Setup Instructions

### Prerequisites:
- Python 3.x installed.
- pip package manager.

### Installation:

1. **Clone the Repository**:
    ```bash
    git clone <repository_url>
    cd socializeProject
    ```

2. **Create a Virtual Environment**:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows: env\Scripts\activate
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply Migrations**:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a Superuser (Admin)**:
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the Development Server**:
    ```bash
    python manage.py runserver
    ```

7. **Access the Application**:
    - **Normal User**: `http://127.0.0.1:8000/login/user/`
    - **Admin User**: `http://127.0.0.1:8000/login/admin_dashboard`
    - **Signup**: `http://127.0.0.1:8000/signup/`

## Application Structure

- **socializeProject/**: Main project directory.
  - **travelapp/**: Django app containing models, views, forms, and templates.
  - **templates/**: HTML templates.
  - **static/**: Static files (CSS, JS, images).
  - **manage.py**: Django's command-line utility.

## Usage

### Normal Users:
1. **Sign Up**: Navigate to `/signup/` to create a new account.
2. **Login**: Go to `/login/user/` and enter your credentials.
3. **Change Password**: After logging in, navigate to `/change-password/` to update your password.
4. **View Posts**: Access the home page to view the latest posts.
5. **Add Comments**: On a post's detail page, add your comments.

### Admin Users:
1. **Login**: Navigate to `/login/admin/` and enter your admin credentials.
2. **Admin Dashboard**: After logging in, access `/admin/dashboard/` to view all users, posts, and comments.
3. **Add Posts**: Use the admin dashboard to create new posts for users.

## Dependencies

- Django==5.1.3
- (Include other dependencies as per `requirements.txt`)

## Deployment

The application is deployed on [Heroku](https://www.render.com/). Access the live application [here](<deployed_application_url>).

## License

This project is licensed under the MIT License.



