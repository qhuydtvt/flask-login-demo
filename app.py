from flask import Flask, render_template, request
from flask_login import LoginManager, login_required, login_user

app = Flask(__name__)
app.config["SECRET_KEY"] = "akjsdhfg oiy4"
login_manager = LoginManager()
login_manager.init_app(app)

class User:
    def __init__(self, username, password):
        self.id = username
        self.username = username
        self.password = password
        self.is_active = True
        self.is_authenticated = True
        self.is_anonymous = False

    def get_id(self):
        return self.id


users = [
    User("don", "dondondon"),
    User("quan", "quanduido"),
    User("admin", "admin")
]


@login_manager.user_loader
def get_user(username):
    print("Ahihi")
    for user in users:
        if user.username == username:
            return user
    return None


@app.route('/')
@login_required
def index():
    return render_template('index.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('login.html')
    elif request.method == "POST":
        form = request.form
        username = form["username"]
        password = form["password"]
        # Login user
        user = get_user(username)
        if user is None:
            return "No such user", 401  # 401 = Unauthorized
        elif user.password != password:
            return "Wrong password", 401  # 401 = Unauthorized
        else:
            login_user(user)
            return "Logged in"


if __name__ == '__main__':
  app.run(port=6969, debug=True)
