from flask import Flask, render_template, request

app = Flask(__name__)

users = []  # список користувачів (у пам'яті)

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

# 🔹 НОВА СТОРІНКА – наприклад, Галерея
@app.route("/gallery")
def gallery():
    images = [
        {"title": "Пейзаж 1", "url": "https://picsum.photos/seed/p1/600/400"},
        {"title": "Пейзаж 2", "url": "https://picsum.photos/seed/p2/600/400"},
        {"title": "Пейзаж 3", "url": "https://picsum.photos/seed/p3/600/400"},
    ]
    return render_template("gallery.html", images=images)

if __name__ == "__main__":
    app.run(debug=True)
