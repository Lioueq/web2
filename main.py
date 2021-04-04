from flask import Flask, render_template, redirect
from data import db_session
from data.users import User
from data.jobs import Jobs
from forms.user import RegisterForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/")
def index():
    pass


def main():
    db_session.global_init("db/mars_explorer.db")
    d = {
        'surname': ['Scott', 'Weir', 'Watney', 'Sunders'],
        'name': ['Ridley', 'Andy', 'Mark', 'Teddy'],
        'age': [21, 23, 22, 25],
        'position': ['captain', 'flight engineer', 'flight engineer', 'flight engineer'],
        'speciality': ['research engineer', 'medic', 'pilot', 'cyber engineer'],
        'address': ['module_1', 'module_2', 'module_2', 'module_2'],
        'email': ['scott_chief@mars.org', 'weir_chief@mars.org', 'watney_chief@mars.org', 'sunders_chief@mars.org']
    }
    for i in range(4):
        user = User()
        user.surname = d['surname'][i]
        user.name = d['name'][i]
        user.age = d['age'][i]
        user.position = d['position'][i]
        user.speciality = d['speciality'][i]
        user.address = d['address'][i]
        user.email = d['email'][i]
        db_sess = db_session.create_session()
        db_sess.add(user)
        db_sess.commit()


if __name__ == '__main__':
    main()
