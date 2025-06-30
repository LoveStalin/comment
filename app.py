from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

client = MongoClient("mongodb+srv://USERNAME:PASSWORD@cluster0.mongodb.net/comment_db?retryWrites=true&w=majority")
db = client["comment_db"]
collection = db["comments"]

@app.route("/")
def home():
    return "API đang chạy rồi nè! 🥳"

@app.route("/comments", methods=["GET"])
def get_comments():
    comments = list(collection.find({}, {"_id": 0}))
    return jsonify(comments)

@app.route("/comments", methods=["POST"])
def post_comment():
    data = request.get_json()
    name = data.get("name", "Ẩn danh")
    message = data.get("message", "").strip()

    if not message:
        return jsonify({"error": "Message is empty!"}), 400

    comment = {"name": name, "message": message, "replies": []}
    collection.insert_one(comment)
    return jsonify({"status": "ok"}), 201

@app.route("/comments/<int:index>/reply", methods=["POST"])
def reply_comment(index):
    data = request.get_json()
    reply = {"name": data.get("name", "Ẩn danh"), "message": data.get("message", "").strip()}

    if not reply["message"]:
        return jsonify({"error": "Reply is empty!"}), 400

    comments = list(collection.find({}, {"_id": 0}))
    if index < 0 or index >= len(comments):
        return jsonify({"error": "Invalid comment index"}), 404

    target_message = comments[index]["message"]

    collection.update_one(
        {"message": target_message},
        {"$push": {"replies": reply}}
    )
    return jsonify({"status": "reply ok"}), 201

if __name__ == "__main__":
    app.run(debug=True)