from flask import Flask, request, redirect
import base64

from db import connect_redis
from utils import encode_url

app = Flask(__name__)
redis_client = connect_redis()

@app.route("/register", methods=["POST"])
def register():
    data = request.json
    clear_url = data["original_url"]
    shorter_endpoint = encode_url(clear_url)
    redis_client.set(shorter_endpoint, clear_url)
    return {
        "status": "success",
        "url": shorter_endpoint
    }

@app.route("/<endpoint>", methods=["GET"])
def redirect_user(endpoint):
    original_endpoint = redis_client.get(endpoint)
    print(original_endpoint)
    if original_endpoint != None:
        return redirect(original_endpoint)
    return "<p>route not found</p>"

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"