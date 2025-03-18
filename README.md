<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Simple Django REST API</title>
</head>
<body>
    <h1 align="center">Simple Django REST API</h1>
    
    <p align="center">
        A REST API built with Django REST Framework that supports CRUD operations for users.
    </p>
    
    <h2>🛠 Tech Stack</h2>
    <ul>
        <li><strong>Python</strong></li>
        <li><strong>Django REST Framework</strong></li>
        <li><strong>SQLite</strong></li>
        <li><strong>Postman</strong> (for testing)</li>
    </ul>
    
    <h2>Features</h2>
    <ul>
        <li><strong>Create a User</strong> – Add a user with name, email, and age.</li>
        <li><strong>Get All Users</strong> – Retrieve a list of all users.</li>
        <li><strong>Get a Single User</strong> – Fetch details of a user by their ID.</li>
        <li><strong>Update a User</strong> – Modify user details using their ID.</li>
        <li><strong>Delete a User</strong> – Remove a user by their ID.</li>
        <li><strong>Error Handling</strong> – Shows errors for invalid requests.</li>
    </ul>
    
    <h2>API Endpoints</h2>
    <table border="1">
        <tr>
            <th>Method</th>
            <th>Endpoint</th>
            <th>Description</th>
        </tr>
        <tr>
            <td>POST</td>
            <td><code>/users/create/</code></td>
            <td>Create a new user</td>
        </tr>
        <tr>
            <td>GET</td>
            <td><code>/users/</code></td>
            <td>Get all users</td>
        </tr>
        <tr>
            <td>GET</td>
            <td><code>/users/&lt;id&gt;/</code></td>
            <td>Get a specific user</td>
        </tr>
        <tr>
            <td>PUT</td>
            <td><code>/users/&lt;id&gt;/update/</code></td>
            <td>Update a user's details</td>
        </tr>
        <tr>
            <td>DELETE</td>
            <td><code>/users/&lt;id&gt;/delete/</code></td>
            <td>Delete a user</td>
        </tr>
    </table>
    
    <h2>Installation & Setup</h2>
    <pre>
        <code>
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
        </code>
    </pre>
    
    <h2>Testing with Postman</h2>
    <p>Use <a href="https://www.postman.com/">Postman</a> to test API requests.</p>
    
    <h2>Contributing</h2>
    <p>Feel free to fork the repository, create a new branch, and submit a pull request.</p>

</body>
</html>
