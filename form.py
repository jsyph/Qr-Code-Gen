from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class QrCodeData(FlaskForm):
    data_input = StringField("Data", validators=[DataRequired()])
