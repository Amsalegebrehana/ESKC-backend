from flask import Blueprint,  request, jsonify
# from werkzeug.security import check_password_hash
from .models import User, Students, Courses, Materials
from flask_bcrypt import Bcrypt
from app import db

bcrypt = Bcrypt()

main = Blueprint('main', __name__)

@main.route('/')
def index():
    print('Hello world!')
    return jsonify({'message': 'Welcome to your Flask main!'})

@main.route('/users')
def get_users():
    print("here")
    users = User.query.all()
    return jsonify([user.username for user in users])

# students section
# regiter students
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
        password=data['password'],
        email=data.get('email'),
        image=data.get('image'),
        grade=data['grade']
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

# get student by id
@main.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    student = Students.query.get(id)

    if student is None:
        return jsonify({'message': 'Student not found'}), 404

    student_data = {
        'id': student.id,
        'first_name': student.first_name,
        'last_name': student.last_name,
        'age': student.age,
        'contact': student.contact,
        'password': student.password,
        'email': student.email,
        'image': student.image,
        'grade': student.grade
    }

    return jsonify(student_data), 200

# update student by id
@main.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    student = Students.query.get(id)

    if student is None:
        return jsonify({'message': 'Student not found'}), 404

    data = request.get_json()

    student.first_name = data.get('first_name', student.first_name)
    student.last_name = data.get('last_name', student.last_name)
    student.age = data.get('age', student.age)
    student.contact = data.get('contact', student.contact)
    student.password = data.get('password', student.password)
    student.email = data.get('email', student.email)
    student.image = data.get('image', student.image)
    student.grade = data.get('grade', student.grade)

    db.session.commit()

    return jsonify({'message': 'Student updated successfully'}), 200

# delete student by id
@main.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    student = Students.query.get(id)

    if student is None:
        return jsonify({'message': 'Student not found'}), 404

    db.session.delete(student)
    db.session.commit()

    return jsonify({'message': 'Student deleted successfully'}), 200

# course section
# get all courses
@main.route('/allcourses', methods=['GET'])
def get_courses():
    courses = Courses.query.all()
    return jsonify([course.repr() for course in courses])

# get courses by id
@main.route('/courses/<int:id>', methods=['GET'])
def get_course(id):
    course = Courses.query.get(id)

    if course is None:
        return jsonify({'message': 'Course not found'}), 404

    course_data = {
        'id': course.id,
        'title': course.title,
        'description': course.description,
        'image': course.image,
        'educationlevelofcourse': course.educationlevelofcourse
    }

    return jsonify(course_data), 200
# get courses by education level
@main.route('/courses/<int:educationlevelofcourse>', methods=['GET'])
def get_course_by_education_level(educationlevelofcourse):
    course = Courses.query.get(educationlevelofcourse)

    if course is None:
        return jsonify({'message': 'Course not found'}), 404

    course_data = {
        'id': course.id,
        'title': course.title,
        'description': course.description,
        'image': course.image,
        'educationlevelofcourse': course.educationlevelofcourse
    }

    return jsonify(course_data), 200

