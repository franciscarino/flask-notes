"""forms for app"""


from flask_wtf import FlaskForm
# import your own form types and validators
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, InputRequired


class RegisterForm(FlaskForm):
    """Form for registering users."""

    username = StringField("Username", validators=[InputRequired()])
    password = StringField("Password", validators=[InputRequired()])
    email = StringField("Email", validators=[InputRequired()])
    first_name = StringField("First Name", validators=[InputRequired()])
    last_name =StringField("Last Name", validators=[InputRequired()])