from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)  # Cho phép truy cập từ bất kỳ domain nào (Vercel, Netlify...)

# Kết nối MongoDB local hoặc MongoDB Atlas
client = MongoClient("mongodb+srv://nguyenxuanthanh1112010:<db_password>@cluster0.4jpjums.mongodb.net/comment_db?retryWrites=true&w=majority&appName=Cluster0")
db = client["comment_db"]
collection = db["comments"]

@app.route("/")
def home():
    return "API đang chạy rồi nè! 🥳"

# API lấy comment
@app.route("/comments", methods=["GET"])
def get_comments():
    comments = list(collection.find({}, {"_id": 0}))  # Ẩn _id khi gửi về
    return jsonify(comments)

# API gửi comment
@app.route("/comments", methods=["POST"])
def post_comment():
    data = request.get_json()
    name = data.get("name", "Ẩn danh")
    message = data.get("message", "").strip()

    if not message:
        return jsonify({"error": "Message is empty!"}), 400

    comment = {"name": name, "message": message}
    collection.insert_one(comment)
    return jsonify({"status": "ok"}), 201

if __name__ == "__main__":
    app.run(debug=True)