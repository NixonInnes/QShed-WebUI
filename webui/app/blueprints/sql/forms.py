from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length

from webui.app.queries import get_all_sql_entities


class ExampleForm(FlaskForm):
    text = StringField(
        "Text: ", default="A default string", validators=[DataRequired(), Length(5)]
    )
    submit = SubmitField()


class CreateSQLEntityForm(FlaskForm):
    name = StringField("Name")
    data = StringField("Data")
    type = SelectField(
        "Data Type",
        choices=(
            (0, "string"),
            (1, "integer"),
            (2, "float"),
            (3, "json")
        )
    )
    parent = SelectField(
        "Parent", 
        choices=(
            [(entity.id, entity.display_name) for entity in get_all_sql_entities()]
        )
    )
    submit = SubmitField("Submit")