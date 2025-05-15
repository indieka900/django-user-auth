# Django Authentication system with JWT Tokens

This is a simple Django project that implements an authentication system using JWT (JSON Web Tokens). It allows users to register, log in, and access protected resources using JWT tokens for authentication.

## Features

- User registration
- User login
- JWT token generation
- User profile retrieval
- User profile update
- Password change
- User deletion
- User list retrieval

## Requirements

- Python 3.12 or higher
- Django 4.0 or higher
- Django REST Framework
- djangorestframework-simplejwt
- djangorestframework

## Installation

1. Clone the repository:

   ```bash
    git clone https://github.com/indieka900/django-user-auth.git
   ```

2. Navigate to the project directory:

   ```bash
   cd django-user-auth
   ```

3. Create a `.env` file in the project root directory and add the following environment variables:

   ```bash
    SECRET_KEY=your_secret_key
    DB_ENGINE=django.db.backends.sqlite3
    DB_NAME=db.sqlite3
    DB_USER=
    DB_PASSWORD=
    DB_HOST=
    ```

    Replace `your_secret_key` with a secret key for your Django project. You can generate a secret key using the following command:

    ```bash
    python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
    ```

4. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

5. Activate the virtual environment:
   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

6. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

7. Apply migrations:

   ```bash
    python manage.py migrate
    ```

8. Create a superuser:

    ```bash
   python manage.py createsuperuser
   ```

9. Run the development server:

   ```bash
    python manage.py runserver
    ```

10. Open your browser and go to `http://localhost:8000/` to access the Swagger UI for the API documentation.

11. You can also access the API endpoints directly using tools like Postman or cURL.

## API Endpoints

### User Registration

- **Endpoint:** `/api/users/`
- **Method:** `POST`
- **Request Body:**

  ```json
  {
    "username": "string",
    "email": "string",
    "password": "string"
  }
  ```

- **Response:**

  ```json
  {
    "user": {
        "id": 1,
        "username": "username",
        "email": "email",
        "profile_picture": null,
        "bio": null,
        "first_name": "",
        "last_name": ""
    },
    "message": "User created successfully"
    }
    ```

### User Login

- **Endpoint:** `/api/users/login/`
- **Method:** `POST`
- **Request Body:**

  ```json
  {
    "email": "string",
    "password": "string"
  }
  ```

- **Response:**

  ```json
  {
    "status": "success",
    "tokens": {
        "refresh": "string",
        "access": "string"
    },
    "user": {
        "id": 1,
        "email": "string"
    }
  }
  ```

### User Profile

- **Endpoint:** `/api/users/profile/`
- **Method:** `GET`
- **Headers:**
  - `Authorization: Bearer <access_token>`
  - `Content-Type: application/json`
- **Response:**

  ```json
  {
    "id": 1,
    "username": "string",
    "email": "string",
    ...
    }
    ```

### User Profile Update

- **Endpoint:** `/api/users/profile/`
- **Method:** `PUT` `PATCH`
*Differentiate between PUT and PATCH*
- **Headers:**
  - `Authorization: Bearer <access_token>`
  - `Content-Type: application/json`
  - **Request Body:**

  ```json
  {
    "bio": "string",
    "first_name": "string",
    ...
  }
  ```

- **Response:**

  ```json
  {
    "id": 1,
    "username": "string",
    "email": "string",
    ...
    }
    ```

### Change Password

- **Endpoint:** `/api/change-password/`
- **Method:** `POST`
- **Headers:**
  - `Authorization: Bearer <access_token>`
  - `Content-Type: application/json`
- **Request Body:**

  ```json
  {
    "old_password": "string",
    "new_password": "string"
  }
  ```

- **Response:**

  ```json
  {
    "detail": "Password changed successfully."
  }
  ```

### User Deletion

- **Endpoint:** `/api/delete-user/`
- **Method:** `DELETE`
- **Headers:**
  - `Authorization: Bearer <access_token>`
  - `Content-Type: application/json`

- **Response:**

  ```json
  {
    "detail": "User deleted successfully."
  }
  ```

### User List Retrieval

- **Endpoint:** `/api/users/`
- **Method:** `GET`
- **Headers:**
  - `Authorization: Bearer <access_token>`
  - `Content-Type: application/json`
- **Response:**

  ```json
  [
    {
      "id": 1,
      "username": "string",
      "email": "string",
      ...
    },
    ...
  ]
  ```

## Contact

For any questions or issues, please contact

- Email : <indiekaj@gmail.com>
- Phone : +254 713 283 900

*This project is developed and maintained by [Joseph Indieka](https://www.linkedin.com/in/joseph-indieka-221557345)*
