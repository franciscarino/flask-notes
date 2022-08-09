"""Flask app."""

from flask import Flask, session, render_template, redirect, flash, jsonify

from flask_debugtoolbar import DebugToolbarExtension
from forms import RegisterForm, LoginForm
from models import db, connect_db, User


app = Flask(__name__)
app.config['SECRET_KEY'] = "YOUR_SECRET"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///flask_notes"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



connect_db(app)
db.create_all()

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

##############################################################################


@app.get("/")
def root():
    """Homepage"""

    return redirect("/register")


@app.route("/register", methods=["GET", "POST"])
def show_register_form():
    """Register/create a user"""

    form = RegisterForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        
        user = User.register(username,password,email,first_name,last_name)
        
        db.session.add(user)
        db.session.commit()
        
        session["username"] = user.username  # keep logged in
        return redirect("/user/<username>")

    else:
        return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Produce login form or handle login."""

    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        # authenticate will return a user or False
        user = User.authenticate(username, password)

        if user:
            session["username"] = user.username # keep logged in
            return redirect(f"/users/{username}")

        else:
            form.username.errors = ["Bad name/password"]

    return render_template("login.html", form=form)


@app.get("/users/<username>")
def show_user_page(username):
    
    if 'username' not in session:
        flash("You must be logged in to view!")
        return redirect("/")

    else:
        user_data = User.query.get(username)
        return render_template('user.html', user_data=user_data)
