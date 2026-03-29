from flask import Flask,url_for,redirect,render_template

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")       #statics routes
def about():
    return "this is About Page"

@app.route("/user/<name>")
def user(name):
    return f"hello {name}"

@app.route("/sum/<int:a>/<int:b>")
def sum(a,b):
    return f"sum is {a+b}"

@app.route("/go")
def go():
    return redirect(url_for("about"))


app.run(debug=True)