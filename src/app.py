from flask import Flask
from routes import init_routes
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Generate a random secret key
init_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
