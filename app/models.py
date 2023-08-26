from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    first_name= db.Column(db.String(100), nullable=False , unique=False)
    last_name= db.Column(db.String(100), nullable=False , unique=True)
    age= db.Column(db.Integer, nullable=False, unique=False)
    contact= db.Column(db.Integer, nullable=False, unique=True)
    password= db.Column(db.String(8), nullable= False, unique= True)
    email = db.Column(db.String(120), nullable= True, unique= True)
    # course_id= db.Column(db.Integer, nullable= False, unique= False, default= 00)
    image= db.Column(db. LargeBinary, nullable= True, unique= False)
    grade= db.Column(db.Integer, nullable= False, unique=False )

    def repr(self):
        return f"Students('{self.first_name}, {self.last_name} | {self.email}')"
    
# class Admins(db.Model):
#     id= db.Column(db.Integer, primary_key= True, nullable= False, autoincrement=True)
#     first_name= db.Column(db.String(100), nullable=False , unique=False)
#     last_name= db.Column(db.String(100), nullable=False , unique=True)
#     password= db.Column(db.String(8), nullable= False, unique= True)
#     email = db.Column(db.String(120), nullable= True, unique= True)
#     image= db.Column(db. LargeBinary, nullable= True, unique= True)
#     contact= db.Column(db.Integer, nullable=False, unique=True)

#     def repr(self):
#         return f"Admins('{self.first_name}, {self.last_name} | {self.email}')"

# class Authors(db.Model):
#     id= db.Column(db.Integer, nullable= False, primary_key= True, autoincrement=True)
#     first_name = db.Column(db.String(100), nullable=False , unique=False)
#     last_name = db.Column(db.String(100), nullable=False , unique=True)
#     password= db.Column(db.String(8), nullable= False, unique= True)
#     email = db.Column(db.String(120), nullable= True, unique= True)
#     image = db.Column(db. LargeBinary, nullable= True, unique= True)
#     contact= db.Column(db.Integer, nullable=False, unique=True)

#     def repr(self):
#         return f"Authors('{self.first_name}, {self.last_name} | {self.email}')"
    
# class Courses(db.Model):
    # id= db.Column(db.Integer, nullable= False, primary_key= True, autoincrement=True)
    # title= db.Column(db.String(150), nullable=False , unique= True)
    # description = db.Column(db.String(150), nullable=False , unique= True)
    # image = db.Column(db.LargeBinary, nullable= True, unique= True)
    # department= db.relationship('Materials', backref= 'department')
    # educationlevelofcourse = db.Column(db.Integer, nullable=False)
    # def repr(self):
    #     return f'Courses("{self.id}, {self.title.upper()}, | ,{self.description}")'
    