# DBMS Lab 01

## Overview

This project is a Django application connected to a MySQL database. It includes functionalities for managing and viewing intern data. The project demonstrates basic CRUD operations, search functionality, and data filtering based on location.

## Features

- **View Interns:** Display a list of interns with details such as InternID, FirstName, LastName, TeamID, JoiningDate, ManagerID, EmailID, PhoneNo, Location, and Stipend.

- **Search Interns:** Search for interns by InternID, ManagerID, or TeamID.

- **Filter by Location:** View interns based on their location (e.g., Bangalore, Delhi, Hyderabad).

- **Django Admin Interface:** Manage the intern data via Django’s built-in admin interface.

## Prerequisites

- Python 3.11+
- Django 4.2+
- MySQL 8.0+
- MySQL client library for Python (`mysqlclient`)

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/yourproject.git
   cd yourproject

2. **Install Dependencies:**

    ```
    pip install -r requirements.txt
    ```

3. **Configure Django Settings:**

    Update core/settings.py with your MySQL database credentials:

    ```
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'xyzcompany',
            'USER': 'root',
            'PASSWORD': 'yourpassword',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }
    ```

4. **Apply Migrations:**

    ```
    python manage.py migrate
    ```

5. **Run the Development Server:**

    ```
    python manage.py runserver
    ```

    Navigate to http://127.0.0.1:8000/ in your browser to see the application.


## Troubleshooting

- **Database Errors**: Ensure that the database and user credentials are correctly configured in settings.py.

- **Migrations Issues**: If you encounter migration issues, you can try resetting migrations with:

```
python manage.py makemigrations
python manage.py migrate
```

-**Permission Issues**: Ensure that you have the necessary permissions for MySQL and Django to access and modify data.


## Contributing

Feel free to fork this repository and make improvements. Please follow the standard Git workflow for contributions and create a pull request for any changes.


### Notes:

- Replace `yourusername/yourproject.git` with your actual GitHub repository URL.
- Replace `yourpassword` with your actual MySQL password.
- Customize the `README.md` with any additional project-specific details or instructions.
- Include any necessary setup or configuration steps relevant to your project.

Let me know if you need any more adjustments!✌️😁






