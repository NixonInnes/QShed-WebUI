from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length

from qshed.client.models.data import SQLEntity

from webui.app import client


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
            [(entity.id, entity.display_name) for entity in client.sql.get_all()]
        )
    )
    submit = SubmitField("Submit")


    def validate(self):
        if not FlaskForm.validate(self):
            return False

        try:
            SQLEntity.get_types()[self.type.data](self.data.data)
        except ValueError:
            self.data.errors.append("Data incompatible with selected data type")
            return False

        return True

