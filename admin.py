import mysql.connector
from flask_bcrypt import Bcrypt

# ---- MySQL Config ----
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "insightbot"
}

bcrypt = Bcrypt()

# ---- Admin Credentials ----
username = "admin"
email = "admin@example.com"
password = "YourAdminPassword"  # CHANGE THIS

# ---- Generate hashed password ----
password_hash = bcrypt.generate_password_hash(password).decode("utf-8")

# ---- Connect to DB ----
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# ---- Insert admin user ----
cursor.execute("""
    INSERT INTO users (username, password_hash, email, is_admin, is_approved)
    VALUES (%s, %s, %s, %s, %s)
""", (username, password_hash, email, 1, 1))

conn.commit()
conn.close()

print(f"Admin user '{username}' created successfully!")