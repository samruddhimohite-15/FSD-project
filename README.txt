REUSE CAMPUS - SIMPLE PYTHON + HTML + POSTGRESQL PROJECT

1. Install Python and PostgreSQL.
2. Open PostgreSQL (pgAdmin or SQL Shell) and create the database:
   CREATE DATABASE reuse_campus;

3. Open app.py and update the PostgreSQL password in DB_CONFIG:
   "password": "root"
   Replace root with your actual PostgreSQL password.

4. Open a terminal in this project folder and install packages:
   pip install -r requirements.txt

5. Run the project:
   python app.py

6. Open this address in your browser:
   http://127.0.0.1:5000

The items table is created automatically when the app starts.

Features:
- View available items
- Add an item
- Remove an item

Note:
This is a simple college project starter. The Remove Item button is not protected by login.
