from flask import Flask

app=Flask(__name__)

@app.route("/")
def home():
    return "hello,Flask!"

@app.route("/about")       #statics routes
def about():
    return "this is About Page"

@app.route("/user/<name>")
def user(name):
    return f"hello {name}"

app.run(debug=True)