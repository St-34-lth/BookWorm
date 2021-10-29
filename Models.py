<<<<<<< HEAD
import csv
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app= Flask(__name__)
app.config["DATABASE_URL"] = 'postgres://jscgdcozzllrcb:f9d3040fa55f18c09257c63af9f0568887f5b4ee9c12adde26fe189743412f26@ec2-46-137-177-160.eu-west-1.compute.amazonaws.com:5432/d72lps0f3so6mt'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://jscgdcozzllrcb:f9d3040fa55f18c09257c63af9f0568887f5b4ee9c12adde26fe189743412f26@ec2-46-137-177-160.eu-west-1.compute.amazonaws.com:5432/d72lps0f3so6mt'

db = SQLAlchemy(app)

class Book(db.Model): 
    __tablename__ = 'books'
    book_id = db.Column(db.Integer, primary_key = True)
    isbn = db.Column(db.String, nullable= False)
    title = db.Column(db.String, nullable= False)
    author = db.Column(db.String, nullable= False)
    pyear = db.Column(db.Integer, nullable= False)
    def __repr__(self):
          return(f'Book:{self.title}, ISBN:{self.isbn}, author:{self.author}, year:{self.pyear}')

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable= False)
    pwd = db.Column(db.String, nullable= False)
    def __repr__(self):
        return(f'User - name:{self.name} id:{self.user_id} ')
        
class Review(db.Model):
    __tablename__='reviews'
    review_id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.user_id))
    book_id = db.Column(db.Integer,db.ForeignKey(Book.book_id))
    review_text = db.Column(db.String, nullable=False)
    user_rating = db.Column(db.Float,nullable=False)
    def __repr__(self):
        return(f'Review for book_id: {self.book_id}, by user_id:{self.user_id}')
    
=======
import csv
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app= Flask(__name__)
app.config["DATABASE_URL"] = 'postgres://jscgdcozzllrcb:f9d3040fa55f18c09257c63af9f0568887f5b4ee9c12adde26fe189743412f26@ec2-46-137-177-160.eu-west-1.compute.amazonaws.com:5432/d72lps0f3so6mt'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://jscgdcozzllrcb:f9d3040fa55f18c09257c63af9f0568887f5b4ee9c12adde26fe189743412f26@ec2-46-137-177-160.eu-west-1.compute.amazonaws.com:5432/d72lps0f3so6mt'

db = SQLAlchemy(app)

class Book(db.Model): 
    __tablename__ = 'books'
    book_id = db.Column(db.Integer, primary_key = True)
    isbn = db.Column(db.String, nullable= False)
    title = db.Column(db.String, nullable= False)
    author = db.Column(db.String, nullable= False)
    pyear = db.Column(db.Integer, nullable= False)
    def __repr__(self):
          return(f'Book:{self.title}, ISBN:{self.isbn}, author:{self.author}, year:{self.pyear}')

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable= False)
    pwd = db.Column(db.String, nullable= False)
    def __repr__(self):
        return(f'User - name:{self.name} id:{self.user_id} ')
        
class Review(db.Model):
    __tablename__='reviews'
    review_id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.user_id))
    book_id = db.Column(db.Integer,db.ForeignKey(Book.book_id))
    review_text = db.Column(db.String, nullable=False)
    user_rating = db.Column(db.Float,nullable=False)
    def __repr__(self):
        return(f'Review for book_id: {self.book_id}, by user_id:{self.user_id}')
    
>>>>>>> e91c249518180045abfd580520895a5a4e9f2171
    