"""forms for app"""

from flask_wtf import FlaskForm
# import your own form types and validators
from wtforms import StringField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, InputRequired



class RegisterForm(FlaskForm):
    """Form for registering users."""

    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])
    email = StringField("Email", validators=[InputRequired()])
    first_name = StringField("First Name", validators=[InputRequired()])
    last_name =StringField("Last Name", validators=[InputRequired()])

class LoginForm(FlaskForm):
    """Form for registering users."""

    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])

class CSRFProtectForm(FlaskForm):
    """Form just for CSRF Protection"""

class NoteForm(FlaskForm):
    """Form for adding new notes."""

    title = StringField("Title", validators=[InputRequired()])
    content = TextAreaField("Content", validators=[InputRequired()])
