# To-Do_Project
A simple, full-featured To-Do list application built with Django. Easily track, create, update, and delete tasks with a clean and intuitive web interface.

## Features

- Create, edit, and delete tasks
- User registration and login (optional)
- Responsive design with Bootstrap (optional)

## Tech Stack

- Backend: Django (Python)
- Database: MySQL 
- Frontend: HTML5, CSS3, Tailwind CSS

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/django-todo-app.git
cd django-todo-app
```                                             
### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```                             
### 3. Install Dependencies

```bash
pip install -r requirements.txt
```             
### 4. Configure Database
Edit the `settings.py` file to configure your MySQL database connection:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```     
### 5. Run Migrations

```bash
python manage.py migrate    
```     
### 6. Create a Superuser (Optional)

```bash 
python manage.py createsuperuser
```     
### 7. Run the Development Server

```bash 
python manage.py runserver
```     
### 8. Access the Application
Open your web browser and go to `http://127.0.0.1:8000/`

## Usage
- Register or log in to your account.
- Create new tasks by filling out the form.
- View, edit, or delete existing tasks from the task list.


