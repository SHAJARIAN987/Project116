from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")

def home():
    name = "Alice"

    age = "9"

    return render_template("index.html", name = name, age = age)

@app.route("/father")

def father():
    name = "Jon"

    age = "43"

    return render_template("father.html", name = name, age = age)

@app.route("/mother")

def mother():
    name = "Sara"

    age = "39"

    return render_template("mother.html", name = name, age = age)

@app.route("/friend")

def friend():
    name = "Steve"

    age = "9"

    return render_template("friend.html", name = name, age = age)

app.run()