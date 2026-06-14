from flask import Flask,render_template,redirect,url_for,session,g,request
from forms import RegistrationForm,LoginForm
from database import get_db,close_db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_session import Session
from functools import wraps

app = Flask(__name__)
app.teardown_appcontext(close_db)
app.config["SECRET_KEY"] = "my_secret_key"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register",methods=["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = form.user.data
        password = form.password.data
        db = get_db()
        conflict = db.execute("""SELECT * FROM users WHERE username = ?""",(user,)).fetchone()

        if conflict is not None:
            form.user.errors.append("Username conflicts with another")
        else:
            db.execute("""INSERT INTO users(username,password) VALUES (?, ?)""",(user,generate_password_hash(password)))
            db.commit()
            return redirect(url_for("login"))
    return render_template("register.html",form=form)

@app.route("/login",methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = form.user.data
        password = form.password.data
        db = get_db()
        matching_user = db.execute("""SELECT * FROM users WHERE username = ?""",(user,)).fetchone()
        if matching_user is None:
            form.user.errors.append("Unknown user id")
        elif not check_password_hash(matching_user["password"],password):
            form.password.errors.append("Incorrect password")
        else:
            session.clear()
            session["user"] = user
            next_page = request.args.get("next")
            if not next_page:
                next_page = url_for("home")
            return redirect(next_page)
    return render_template("login.html",form=form)
        
    
