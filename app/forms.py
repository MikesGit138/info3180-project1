from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField, FileField
from wtforms.validators import DataRequired

class PropertyForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    bedrooms = StringField('Number of Bedrooms', validators=[DataRequired()])
    bathrooms = StringField('Number of Bathrooms', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    type = SelectField('Type', choices=[('house', 'House'), ('apartment', 'Apartment')], validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    photo = FileField('Photo', validators=[DataRequired()])
    submit = SubmitField('Add Property')
