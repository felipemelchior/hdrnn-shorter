from flask import request, redirect, abort, jsonify, send_from_directory
from utils import encode_url

def register_routes(app):
    @app.route("/", methods=["GET"])
    def short_url():
        return send_from_directory("static", "index.html")

    @app.route("/register", methods=["POST"])
    def register():
        data = request.get_json()
        if not data or "original_url" not in data:
            abort(400, "Missing 'original_url'")
        clear_url = data["original_url"]
        shorter_endpoint = encode_url(clear_url)
        try:
            app.redis_client.set(shorter_endpoint, clear_url)
        except Exception as e:
            app.logger.error(f"Redis error: {e}")
            abort(500, "Internal Server Error")
        return {
            "status": "success",
            "url": shorter_endpoint
        }

    @app.route("/<endpoint>", methods=["GET"])
    def redirect_user(endpoint):
        original_endpoint = app.redis_client.get(endpoint)
        app.logger.debug(f"Redirecting to: {original_endpoint}")
        if original_endpoint != None:   
            return redirect(original_endpoint)
        return {"error": "route not found"}, 404
