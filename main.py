from flask import Flask, render_template, redirect
from data import db_session
from data.users import User
from data.jobs import Jobs
from forms.user import RegisterForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/")
def index():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return render_template("index.html", jobs=jobs)


def main():
    db_session.global_init("db/mars_explorer.db")
    app.run(port=8080)


if __name__ == '__main__':
    main()
