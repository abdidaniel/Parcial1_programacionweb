from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, TimeField, SelectField, IntegerField, BooleanField
from wtforms.validators import DataRequired, Length, NumberRange

class EventForm(FlaskForm):
    title = StringField('Título', validators=[DataRequired(), Length(min=5, max=100)])
    description = TextAreaField('Descripción', validators=[DataRequired(), Length(min=10)])
    date = DateField('Fecha', format='%Y-%m-%d', validators=[DataRequired()])
    time = TimeField('Hora', format='%H:%M', validators=[DataRequired()])
    location = StringField('Ubicación', validators=[DataRequired()])
    category = SelectField('Categoría', choices=[(cat, cat) for cat in ['Tecnología', 'Académico', 'Cultural', 'Deportivo', 'Social']], validators=[DataRequired()])
    max_attendees = IntegerField('Máximo de Asistentes', validators=[DataRequired(), NumberRange(min=1)])
    featured = BooleanField('Destacado')

class RegistrationForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired()])
    email = StringField('Correo Electrónico', validators=[DataRequired()])