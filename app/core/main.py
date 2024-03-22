from app import app, db
from flask import request, jsonify
from app.models.user import User
from flask_jwt_extended import create_access_token, jwt_required

@app.route('/')
@jwt_required()
def main_page():
    return '<h1>Main page</h1>'

@app.route('/register', methods=['POST'])
def register():
    if request.is_json:
        email = request.json['email']
        user_account = User.query.filter_by(email=email).first()
        if user_account:
            return jsonify(message='User account already exists!'), 409
        else:
            first_name = request.json['first_name']
            last_name = request.json['last_name']
            email = request.json['email']
            password = request.json['password']
            user = User(fname=first_name, lname=last_name, email=email, password=password)
            db.session.add(user)
            db.session.commit()
            return jsonify(message='User account has been successfully created!'), 201
    else:
        email = request.form['email']
        user_account = User.query.filter_by(email=email).first()
        if user_account:
            return jsonify(message='User account already exists!'), 409
        else:
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            email = request.form['email']
            password = request.form['password']
            user = User(fname=first_name, lname=last_name, email=email, password=password)
            db.session.add(user)
            db.session.commit()
            return jsonify(message='User account has been successfully created!'), 201
    
@app.route('/login', methods=['POST'])
def login():
    if request.is_json:
        email = request.json['email']
        password = request.json['password']
    else:
        email = request.form['email']
        password = request.form['password']
    
    user_account = User.query.filter_by(email=email, password=password).first()

    if user_account:
        user_jwt_token = create_access_token(identity=email)
        return jsonify(message='Login is successful!', access_token=user_jwt_token)
    else:
        return jsonify(message='Email or password is incorrect!'), 401