from flask import Blueprint,  request, jsonify
# from werkzeug.security import check_password_hash
from .models import User, Students
from flask_bcrypt import Bcrypt
from app import db

bcrypt = Bcrypt()

main = Blueprint('main', __name__)

@main.route('/')
def index():
    print('Hello world!')
    return jsonify({'message': 'Welcome to your Flask app!'})

@main.route('/users')
def get_users():
    print("here")
    users = User.query.all()
    return jsonify([user.username for user in users])



@main.route('/register', methods=['POST'])
def register():
    data = request.json

    # Check if the email already exists
    existing_student = Students.query.filter_by(email=data['email']).first()
    if existing_student:
        return jsonify({'message': 'Email already registered'}), 400

    new_student = Students(
        first_name=data['first_name'],
        last_name=data['last_name'],
        age=data['age'],
        contact=data['contact'],
        password=bcrypt.generate_password_hash(data['password']),
        email=data['email'],
        grade=data['grade']
        # Other fields
    )

    db.session.add(new_student)
    db.session.commit()

    return jsonify({'message': 'Registration successful'}), 201

@main.route('/login', methods=['POST'])
def login():
    data = request.json
    student = Students.query.filter_by(email=data['email']).first()

    if not student or not bcrypt.check_password_hash(student.password, data['password']):
        return jsonify({'message': 'Invalid email or password'}), 401


    # You can create a JWT token for authentication here

    return jsonify({'message': 'Login successful'})

# get all students
@main.route('/allstudents', methods=['GET'])
def get_students():
    students = Students.query.all()
    return jsonify([student.repr() for student in students])




