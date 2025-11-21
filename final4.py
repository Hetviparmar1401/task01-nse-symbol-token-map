from flask import Flask, request

app = Flask(__name__)

# GET method
@app.route("/hello", methods=["GET"])
def hello():
    return {"message": "Hello, Flask API works!"}

# POST method
@app.route("/hello_post", methods=["POST"])
def hello_post():
    data = request.get_json()
    if not data or "name" not in data:
        return {"error": "Send JSON with 'name' key"}, 400
    name = data["name"]
    return {"message": f"Hello, {name}! POST API works!"}

if __name__ == "__main__":
    app.run(debug=True)
