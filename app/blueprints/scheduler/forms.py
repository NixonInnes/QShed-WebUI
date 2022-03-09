from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length


class ExampleForm(FlaskForm):
    text = StringField(
        "Text: ", default="A default string", validators=[DataRequired(), Length(5)]
    )
    submit = SubmitField()


class NewScheduleForm(FlaskForm):
    interval = IntegerField("Interval")
    url = StringField("URL")
    method = SelectField("Method", choices=("get", "post"))
    params = TextAreaField("URL Parameters")
    data = TextAreaField("Request Data")
    headers = TextAreaField("Request Headers")
    submit = SubmitField("Submit")
