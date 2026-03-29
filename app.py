from flask import Flask,url_for,redirect,render_template,request

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
    if request.method=="POST":
        name=request.form["username"]
        age=request.form["age"]
        return f"hello {name} you are {age} years old"
    return render_template("index.html")



@app.route("/about")       #statics routes
def about():
    return render_template("about.html")

@app.route("/user/<name>")
def user(name):
    return render_template("index.html",username=name)

@app.route("/sum/<int:a>/<int:b>")
def sum(a,b):
    return f"sum is {a+b}"

@app.route("/go")
def go():
    return redirect(url_for("about"))


app.run(debug=True)