from flask_sqlalchemy import SQLAlchemy

# 


class Config:
    SECRET_KEY =" os.getenv('SECRET_KEY')"
    
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
# SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
# SQLALCHEMY_TRACK_MODIFICATIONS = False
