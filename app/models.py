from app import db


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
# user is based on role(admin, author)
class User(db.Model):
    id= db.Column(db.Integer, primary_key= True, nullable= False, autoincrement=True)
    first_name= db.Column(db.String(100), nullable=False , unique=False)
    last_name= db.Column(db.String(100), nullable=False , unique=True)
    password= db.Column(db.String(200), nullable= False, unique= True)
    email = db.Column(db.String(120), nullable= True, unique= True)
    image= db.Column(db. LargeBinary, nullable= True, unique= True)
    contact= db.Column(db.Integer, nullable=False, unique=True)
    # role enum('admin', 'author')
    role= db.Column(db.Enum('admin', 'author'), nullable= False, unique= False)
   

    def repr(self):
        return f"Admins('{self.first_name}, {self.last_name} | {self.email}')"

class Materials(db.Model):
    id= db.Column(db.Integer, nullable= False, primary_key= True, autoincrement=True)
    course_id= db.Column(db.Integer, db.ForeignKey('courses.id'), nullable= False, unique= False)
    author_id= db.Column(db.Integer, db.ForeignKey('user.id'), nullable= False, unique= False)
    title= db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(150), nullable=False)
    image = db.Column(db.LargeBinary, nullable= True)
    type_of_material = db.Column(db.Enum('video', 'pdf', 'quiz'), nullable= False, unique= False)
    # file should be saved on the server
    file = db.Column(db.String(100), nullable=True)

class Courses(db.Model):
    id= db.Column(db.Integer, nullable= False, primary_key= True, autoincrement=True)
    title= db.Column(db.String(150), nullable=False )
    description = db.Column(db.String(150), nullable=False )
    image = db.Column(db.LargeBinary, nullable= True)
    department= db.relationship('Materials', backref= 'department')
    educationlevelofcourse = db.Column(db.Integer, nullable=False)
  

    def repr(self):
        return f'Courses("{self.id}, {self.title.upper()}, | ,{self.description}")'
    
