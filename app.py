"""Flask app."""

from flask import Flask, session, render_template, redirect, flash, jsonify

from flask_debugtoolbar import DebugToolbarExtension
from forms import RegisterForm, LoginForm, CSRFProtectForm, NoteForm
from models import db, connect_db, User, Note

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
#Users

@app.get("/")
def root():
    """Bring user to register page"""
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
        return redirect(f"/users/{username}")

    else:
        return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Produce login form or handle login."""

    if 'username' in session:

        return redirect(f"/users/{session['username']}")

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
    """Display user page or redirect to homepage"""

    form = CSRFProtectForm()

    if 'username' not in session or username != session['username']:
        flash("You must be logged in to view!")
        return redirect("/")

    else:
        user_data = User.query.get(username)

        #TODO:
        #Show all of the notes a user has given.
        #For each note, display with a link to a form to edit the note and a button to delete the note.
        #Have a link that sends you to a form to add more notes and a button to delete the entire user account, including their notes.


        return render_template('user.html', user_data=user_data, form=form)


@app.post("/logout")
def logout():
    """Logs user out and redirects to homepage."""

    form = CSRFProtectForm()

    if form.validate_on_submit():
        # Remove "user_id" if present, but no errors if it wasn't
        session.pop("username", None)

    return redirect("/")


@app.post("/users/<username>/delete")

##############################################################################
#Notes

@app.route("/users/<username>/notes/add", methods=["GET", "POST"])
def handle_add_note(username):
    """Display add note form, add new note"""

    if 'username' not in session or username != session['username']:
        flash("You must be logged in to view!")

        return redirect("/")

    form = NoteForm()

    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data

        new_note = Note(title=title, content=content, owner=username)

        db.session.add(new_note)
        db.session.commit()

        return redirect(f"/users/{username}")

    else:
        return render_template("register.html", form=form)



# @app.route("/notes/<note-id>/update", methods=["GET", "POST"])


# @app.post("/notes/<note-id>/delete")