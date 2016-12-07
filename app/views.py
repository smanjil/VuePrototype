
from flask import render_template, request
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
    print data['username'], data['password']
    return 'done'
