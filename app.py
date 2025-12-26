from flask import Flask, render_template, request

app = Flask(__name__)
users = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        users.append({"name": name, "email": email, "message": message})

        return render_template("result.html", name=name, email=email, message=message)

    return render_template("register.html")

@app.route("/users")
def show_users():
    return render_template("users.html", users=users)

if __name__ == "__main__":
    app.run(debug=True)