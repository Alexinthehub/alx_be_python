# Django Role-Based Access Control Project

This project implements role-based access control using Django. It includes:
- A custom `UserProfile` model linked to Django's User model with a `role` field.
- Views restricted by user role (Admin, Librarian, Member).
- URL patterns for each role-based view.
- HTML templates for each role.

## Setup
1. Create and activate a virtual environment:
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies:
   ```sh
   pip install django
   ```
3. Run migrations:
   ```sh
   python manage.py migrate
   ```
4. Create a superuser:
   ```sh
   python manage.py createsuperuser
   ```
5. Start the development server:
   ```sh
   python manage.py runserver
   ```

## App Structure
- `django_models/models.py`: UserProfile model
- `django_models/views.py`: Role-based views
- `django_models/urls.py`: URL patterns
- `django_models/templates/`: HTML templates

## Usage
- Log in as a user with the appropriate role to access each view.
