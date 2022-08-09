"""Flask app."""

from flask import Flask, url_for, render_template, redirect, flash, jsonify

from flask_debugtoolbar import DebugToolbarExtension
from forms import RegisterForm
from models import db, connect_db


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


@app.get("/register", methods=["GET", "POST"])
def show_register_form():
    """Register/create a user"""

    form = RegisterForm()


    if

    else:
        return render_template("register.html", form=form)


@app.get("/login")


@app.post("/login")


@app.get("/secret")