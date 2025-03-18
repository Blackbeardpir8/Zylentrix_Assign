# Django REST API for User Management

A simple REST API built with **Django REST Framework** that allows users to be created, retrieved, updated, and deleted (CRUD operations). It uses **SQLite** as the database.

## Tech Stack
- **Python**
- **Django REST Framework**
- **SQLite**
- **Postman** (for testing)

## Features
- **Create a User** – Add a user with `name`, `email`, and `age`.
- **Get All Users** – Retrieve a list of all users.
- **Get a Single User** – Fetch user details by ID.
- **Update a User** – Modify user details by ID.
- **Delete a User** – Remove a user by ID.
- **Error Handling** – Returns errors for invalid requests.

## API Endpoints

| Method  | Endpoint               | Description               |
|---------|------------------------|---------------------------|
| **POST**   | `/users/create/`       | Create a new user         |
| **GET**    | `/users/`              | Get all users             |
| **GET**    | `/users/<id>/`         | Get a specific user       |
| **PUT**    | `/users/<id>/update/`  | Update a user's details   |
| **DELETE** | `/users/<id>/delete/`  | Delete a user            |

## Installation & Setup
```sh
# Clone the repository
git clone https://github.com/your-username/django-rest-api.git
cd django-rest-api

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start the server
python manage.py runserver
