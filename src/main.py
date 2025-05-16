from flask import Flask
from routes.url_routes import register_routes
from db import connect_redis

def create_app():
    app = Flask(__name__)
    app.redis_client = connect_redis()
    register_routes(app)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)