from flask import Flask
from markupsafe import escape
from flask import request

app = Flask(__name__)


# # http://localhost:5000
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


# PARAMS ---------------
# http://localhost:5000/user/lukas
@app.route("/user/<username>")
def show_user_profile(username):
    # show the user profile for that user
    return f"User {escape(username)}"


# http://localhost:5000/post/1
@app.route("/post/<int:post_id>")
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f"Post {post_id}"


# SUBPATH ---------------
# http://localhost:5000/path/blabla/aaa
@app.route("/path/<path:subpath>")
def show_subpath(subpath):
    # show the subpath after /path/
    return f"Subpath {escape(subpath)}"


# GET vs. POST ---------------
# http://localhost:5000/login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return "login POST"
    else:
        return "login GET"


# JSON ---------------
# http://localhost:5000/me
@app.route("/me")
def me_api():
    return {
        "username": "test1",
        "theme": "light",
        "image": "http://test.com/test.jpg",
    }
