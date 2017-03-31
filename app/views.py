
from flask import render_template, request, redirect, url_for
from app import app, db
from .models import User
import json

@app.route('/')
def index():
    return render_template(
        'index.html',
        title='Home'
    )

@app.route('/login', methods=['POST'])
def login():
    data = json.loads(request.data)
    username, password = data['username'], data['password']

    user_row = User.query.filter(User.username == username, User.password == password).first()
    if user_row is not None:
        print user_row.role

    if user_row.role == 'admin':
        return redirect(url_for('admin'))
    elif user_row.role == 'operator':
        return redirect(url_for('operator'))

    return None

@app.route('/admin')
def admin():
    return render_template(
        'admin.html',
        title='Admin'
    )

@app.route('/operator')
def operator():
    return render_template(
        'operator.html',
        title='Operator'
    )
