from api import app, db

app.app_context().push()
db.create_all()
print("Database created successfully.")
