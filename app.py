from flask import Flask,render_template,redirect,url_for
from forms import RegistrationForm
from database import get_db,close_db
from werkzeug.security import generate_password_hash,check_password_hash

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register",methods=["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = user.form.data
        password = password.form.data
        db = get_db()
        conflict = db.execute("""SELECT * FROM users WHERE username = ?""",(user,)).fetchone()

        if conflict is not None:
            form.user.errors.append("Username conflicts with another")
        else:
            db.execute("""INSERT INTO users(username,password) VALUES (?, ?)""",(user,generate_password_hash(password)))
            db.commit()
            return redirect(url_for("login"))
    return render_template("register.html",form=form)