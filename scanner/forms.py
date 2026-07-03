from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class TargetForm(FlaskForm):
    target = StringField('Enter IP Address or Domain Name', validators=[DataRequired()])
    submit = SubmitField('Scan')