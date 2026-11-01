from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__)

# Update these details to match your PostgreSQL setup
DB_CONFIG = {
    "host": "localhost",
    "database": "reuse_campus",
    "user": "postgres",
    "password": "root",
    "port": 5432
}

def get_connection():
    return psycopg2.connect(**DB_CONFIG)

def create_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS items (
            id SERIAL PRIMARY KEY,
            student_name VARCHAR(100) NOT NULL,
            item_name VARCHAR(150) NOT NULL,
            description TEXT,
            category VARCHAR(50)
        )
    """)
    conn.commit()
    cur.close()
    conn.close()

@app.route("/")
def home():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT id, student_name, item_name, description, category
        FROM items
        ORDER BY id DESC
    """)
    items = cur.fetchall()
    cur.close()
    conn.close()
    return render_template("index.html", items=items)

@app.route("/add", methods=["GET", "POST"])
def add_item():
    if request.method == "POST":
        student_name = request.form["student_name"].strip()
        item_name = request.form["item_name"].strip()
        description = request.form["description"].strip()
        category = request.form["category"]

        if student_name and item_name:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO items (student_name, item_name, description, category)
                VALUES (%s, %s, %s, %s)
            """, (student_name, item_name, description, category))
            conn.commit()
            cur.close()
            conn.close()
            return redirect(url_for("home"))

    return render_template("add_item.html")

@app.route("/delete/<int:item_id>", methods=["POST"])
def delete_item(item_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM items WHERE id = %s", (item_id,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for("home"))

if __name__ == "__main__":
    create_table()
    app.run(debug=True)
