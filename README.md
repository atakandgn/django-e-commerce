# Django E-Commerce

![E-Commerce](https://github.com/atakandgn/django-e-commerce/assets/108396649/f2898d58-68cf-4612-b0c2-02efef357f79)

> This Django project is a sophisticated E-Commerce platform that facilitates seamless product transactions. Users can browse product listings, view detailed product information, and utilize a powerful search functionality.

---

## Table of Contents

- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Database Configuration](#database-configuration)
  - [Deploying the Website on Render.com](#deploying-the-website-and-database)
  - [Demo](#demo)
  - [Clone the Repository](#clone-the-repository)
- [Contact Information](#contact-information)

---

## Project Structure

- **buy_sell_website:** Primary Django app for the E-Commerce website.
- **django_e_commerce:** Django project settings and configuration.

## Getting Started

Follow these steps to run the project examples.

### Requirements

- Python
- Django
- virtualenv (optional)

### Installation

1. Navigate to the project directory: `cd django_e_commerce`

2. If you are using virtualenv, activate your virtual environment: `source venv/Scripts/activate`

3. Install the required dependencies: `pip install -r requirements.txt`

4. Create the database: `python manage.py migrate`

5. Start the Django development server: `python manage.py runserver`

The project should be accessible at [http://127.0.0.1:8000](http://127.0.0.1:8000).

### Database Configuration

This project uses PostgreSQL as the database. Set up your PostgreSQL configuration in the `settings.py` file located in the `django_e_commerce` directory. Update the `DATABASES` setting with your PostgreSQL database information.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'your_neon_host_url',
        'PORT': 'your_neon_port',
        'OPTIONS': {'sslmode': 'require'},
    }
}
```
![products](https://github.com/atakandgn/django-e-commerce/assets/108396649/32707d00-9805-4258-bb64-63ef5e8e862c)
![categories](https://github.com/atakandgn/django-e-commerce/assets/108396649/5618cf34-cda3-4c18-aaa0-7b8ce4d7cfb3)
![subcategories](https://github.com/atakandgn/django-e-commerce/assets/108396649/25d7690e-27bf-46dc-885a-4bc2f3b333aa)


### Deploying the Website and Database

- **Website Deployment on Render.com:**
  1. Create an account on [Render.com](https://render.com).
  2. Deploy the Django E-Commerce website by creating a new web service on Render.com.
  3. Follow the instructions provided by Render.com for deploying a Django application.
  4. Configure environment variables on Render.com, including PostgreSQL credentials.

- **Database Deployment on Neon.tech:**
  1. Host your PostgreSQL database on [Neon.tech](https://console.neon.tech/app).
  2. Set up a Neon database instance and obtain the necessary connection details.
  3. Update the `settings.py` file in the `django_e_commerce` directory with the Neon PostgreSQL configuration.


### Demo

- Explore the deployed E-Commerce website running on Render.com at [https://djangowebapp.onrender.com](https://djangowebapp.onrender.com).

### Clone the Repository

1. Clone this repository: `git clone https://github.com//atakandgn/django-e-commerce`

2. Navigate to the project directory: `cd async-view-project`

3. If you are using virtualenv, activate your virtual environment: `source myenv/bin/activate`

4. Install the required dependencies: `pip install requirements.txt`

5. Create the database: `python manage.py migrate`

6. Start the Django development server: `python manage.py runserver`

The project should now be accessible at [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Contact Information

For communication, reach out to atakandogan.info@gmail.com or connect on [LinkedIn](https://www.linkedin.com/in/atakandoan/).

---

*Thank you for choosing Django E-Commerce for your project!*
