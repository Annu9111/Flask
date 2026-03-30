from flask import Blueprint, render_template
from .models import User
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/add/<name>')
def add_user(name):
    user = User(name=name)
    db.session.add(user)
    db.session.commit()
    return f"{name} added!"

@main.route('/users')
def get_users():
    users = User.query.all()
    return "<br>".join([user.name for user in users])