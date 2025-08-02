# Django REST Framework Project

A basic Django project with Django REST Framework integration.

## Features

- Django 5.2.4
- Django REST Framework 3.16.0
- Simple API endpoint with CRUD operations

## Setup

1. Clone the repository
2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```
   python manage.py migrate
   ```
5. Start the development server:
   ```
   python manage.py runserver
   ```

## API Endpoints

- API Root: `/api/`
- Images List/Create: `/api/images/`
- Image Detail/Update/Delete: `/api/images/{id}/`

## Project Structure

- `core/` - Main project settings
- `api/` - Django app with REST Framework implementation
  - `models.py` - Data models
  - `serializers.py` - REST Framework serializers
  - `views.py` - API views
  - `urls.py` - API URL routing
