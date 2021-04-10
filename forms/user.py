from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class AddJobForm(FlaskForm):
    job = StringField('Описание работы', validators=[DataRequired()])
    team_leader = StringField('Id руководителя', validators=[DataRequired()])
    work_size = IntegerField('Объем работы в часах', validators=[DataRequired()])
    collaborators = StringField('Список id участников', validators=[DataRequired()])
    is_finished = BooleanField('Работа завершена', validators=[DataRequired()])
    submit = SubmitField('Войти')
