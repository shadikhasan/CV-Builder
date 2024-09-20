
![Screenshot (21)](https://github.com/user-attachments/assets/a03346e8-76e3-4e42-96d8-38e3edf90f84)
![Screenshot (22)](https://github.com/user-attachments/assets/82f3dd3f-c78c-45f3-94c4-ad63f76b8ac9)
![Screenshot (23)](https://github.com/user-attachments/assets/ab887227-3ddb-4d66-aa7f-6a8f2df2bb8c)
![Screenshot (24)](https://github.com/user-attachments/assets/c3d6ac0b-ebd4-4d67-ae9c-0fd9d8af44f2)
![Screenshot (25)](https://github.com/user-attachments/assets/e6131761-45f0-49c3-b1a0-79d61ae99ab7)
![Screenshot (26)](https://github.com/user-attachments/assets/480e3a08-001b-4b66-9bab-36b27d4da2cd)

# 1. Initial Setup

## Prerequisites

Make sure you have the following installed:

- **Python 3.8+**
- **pip** (Python package manager)
- **Docker** (optional, if using Docker)
- **Git** (version control)

## Setup Instructions

### 1. Clone the Repository

First, clone the repository to your local machine and navigate to the project directory:

```
git clone https://github.com/shadikhasan/CV-Builder-Django.git
cd CV Builder Django
```

### 2. Create a Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Apply Database Migrations

```
python manage.py migrate
```

### 5.1. Create a Superuser (Optional)

```
python manage.py createsuperuser
```

### 5.2 Initial super user by command(Optional)

```
python manage.py init_superuser
```

### 6. Start the Development Server

```
python manage.py runserver
```

The API will then be available at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

# 2. Using docker

### Build Docker file

```
docker-compose build
```

### To start project, run:

```
docker-compose up
```

The API will then be available at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

### To Log in To the Dashboard(Frontend) or Admin Panel

#### Username

```
admin
```

#### Password

```
admin
```

---

## Development Guide

### Create Project

```
docker-compose run app sh -c "django-admin startproject NewProject ."
```

### Create New App

```
docker-compose run --rm app sh -c "python manage.py startapp newApp"
```

### Create Super User

```
docker-compose run --rm app sh -c "python manage.py createsuperuser"
```

### Initial super user by command(Optional)

```
docker-compose run --rm app sh -c "python manage.py init_superuser"
```

### Make Migrations

```
docker-compose run app sh -c "python manage.py makemigrations"
```
