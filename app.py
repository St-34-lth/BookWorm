from flask import Flask, session, render_template , jsonify, request, redirect, url_for
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from Models import Book, User, Review
import secrets
import requests,json
import xml.etree.ElementTree as ET 
from xml.dom import minidom

#configure Flask app
app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = ''
app.config['FLASK_ENV'] = 'development'
app.config['SQLALCHEMY_TRACE_MODIFICATIONS'] = True  #to set debug mode ---> $env:FLASK_ENV='development' in powershell 
app.config["DATABASE_URL"] = ''

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

# Check for environment variable
#if not app.config["DATABASE_URL"]:
 #   raise RuntimeError("DATABASE_URL is not set")

# Set up database
db = SQLAlchemy(app)

#set up secret key & user session data 
app.secret_key = ''

@app.route("/",methods=['GET','POST'])
def index():
    if request.method=='GET':
        if session.get('logged_in'):
            print(session.get('logged_in'))
            
            return render_template('index.html',uname=(User.query.filter_by(user_id=session.get('user_id')).first().name))
        else:
            print(session.get('logged_in'))   
            return render_template('base.html')

@app.route("/search_results", methods=['POST','GET'])
def search_results():

    if request.method=='POST':
            
            #fetch search text
            searched = '%' + str(request.form.get('searchform'))+'%'
                                                      
            #sql query
            book_data = db.session.execute("SELECT * from books WHERE title ilike :searched or author ilike :searched or isbn ilike :searched",
                        {"searched": searched}).fetchall()
            print(book_data)  
            #unpack the resultproxy object
            # NOTE: if i can abstract indices I can get this to work with more options to sort the list
            
            books = {}
            for book in book_data:
                 books[book[2]] = dict(book_id=book[0],isbn=book[1],author=book[3],pyear=book[4])
                
            if books == None:
                return render_template('error.html')
            
            return render_template('results.html',searched=searched.replace('%','') , result=books) 

@app.route('/search_results/<string:titlename>',methods=['GET','POST'])
def search_handler(titlename):
    title = Book.query.filter_by(title=titlename).first()
    print(title) 
    user_id = session.get('user_id')
    reviewList = Review.query.filter_by(book_id=title.book_id).all()
    ratings = PullRating(search=title.title)
    
    for review in reviewList:
        if review.user_id == user_id:
            message= 'You cant add more reviews.'
            session['has_comment'] = True
            break
        else:
            session['has_comment'] = False
            message=''
    if request.method =='POST':    
        review_string = request.form.get('review_typer')
        user_rating = float(request.form.get('rating_slider'))
        user_review = Review(review_text=review_string,book_id=title.book_id, user_id=user_id,user_rating=user_rating)

        if reviewList != None:
            if session.get('has_comment'):
                return render_template('result.html',title=title.title,isbn=title.isbn,author=title.author,pyear=title.pyear,ID=title.book_id,rate_num=ratings[1],rate=ratings[0],reviewList=reviewList,message=message)
            
            else:                
                db.session.add(user_review)                    
                db.session.commit()
                reviewList = Review.query.filter_by(book_id=title.book_id).all()
                    
                return render_template('result.html',title=title.title,isbn=title.isbn,author=title.author,pyear=title.pyear,ID=title.book_id,rate_num=ratings[1],rate=ratings[0],reviewList=reviewList) 
      

        else:                
            db.session.add(user_review)                    
            db.session.commit()
            reviewList = Review.query.filter_by(book_id=title.book_id).all()
            return render_template('result.html',title=title.title,isbn=title.isbn,author=title.author,pyear=title.pyear,ID=title.book_id,rate_num=ratings[1],rate=ratings[0],reviewList=reviewList) 
   
    elif request.method=='GET':
        return render_template('result.html',title=title.title,isbn=title.isbn,author=title.author,pyear=title.pyear,ID=title.book_id,rate_num=ratings[1],rate=ratings[0],reviewList=reviewList)
     
@app.route('/new_user', methods =['GET','POST'])
def new_user():
    
    if request.method =='GET':
        return render_template('register.html',title='Registration')                
    
    if request.method =='POST': 

        #form query 
        uname = str(request.form.get('uname'))
        pwd = str(request.form.get('pwd'))
        #Query registered users 
        userList = User.query.all()
        print(userList)
        #create new User object
        new_user = User(name=uname,pwd=pwd)
        
        if (new_user):
            if len(userList)>0:
                for regUser in userList:
                    if regUser.name == new_user.name:
                            return render_template('error.html', message='Username already exists.')
                    else:
                        print(new_user)
                        db.session.add(new_user)
                        db.session.commit()
                        return render_template('success.html',message='Registration successful.')
            else:
                print(new_user)
                db.session.add(new_user)
                db.session.commit()
                return render_template('success.html',message='Registration successful.')
        else:
            return render_template('error.html', message='Registration failed.')
 
@app.route('/import', methods=['GET','POST'])
def file_handler():

    return render_template('import.html')

@app.route('/login', methods=['GET','POST'])
def login_handler():
    if request.method =='POST':
          
        if session.get('logged_in') == None or session.get('logged_in') == False:
             
            uname = str(request.form.get('uname'))
            pwd = str(request.form.get('pwd'))
                #Create User object with given name and pwd & Get list of registered users
            session['user_id'] = User.query.filter_by(name=uname,pwd=pwd).first().user_id
            
            userList = User.query.all()
            
            for user in userList:
                if user.user_id == session.get('user_id'):
                    
                    session['logged_in']= True
                    print(session.get('logged_in'))   
                    break
              
            return redirect(url_for('index'))
        else:
              
            return redirect(url_for('index'))
    else:
        
        return render_template('login.html')

@app.route('/exit', methods=['POST','GET'])
def logout(): ##to implement input of user it has to logout
    
    if request.method =='POST':    
        
        if session['logged_in']:
                session['logged_in'] = False
                session['USERNAME'] = None
                session['PASSWORD'] = None 
                session['user_id'] = None
                return render_template('base.html')
        else:
            return render_template('base.html')
    else:
        return render_template('base.html') 
      
def format_searchable(text):
    textLength = len(text)
    reformated_text = {}
    if (textLength > 3):
        textDivisor = textLength / 3 
        for i in text:
            if i == '':
                continue 
            if i.isalnum():
                pairs = 0
                divisor = 3
                while pairs <= textDivisor:
                    three_letters = text[(divisor-3):divisor]
                    reformated_text[str(pairs)] = Book.query.filter(Book.title.ilike('%'+three_letters+'%'))
                    pairs += 1
                    divisor += 3
    else:
        return [f'%{text}%']
    return reformated_text

def PullRating(search,*args):
  #set up payload parameters
  key = '9QfFG2IhANpg4EixwogLA'
  payload = {'q':search, 'key':key}
  res = requests.get(f"https://www.goodreads.com/search/index.xml", params=payload)
  
  #parse the xml response to a DOM tree
  xmldom = minidom.parseString(res.content)
  
  #print(xmldom.toprettyxml())

  #get the value of the average rating childNode
  avg_rate = xmldom.getElementsByTagName('average_rating')[0].childNodes[0].nodeValue
  rate_count = xmldom.getElementsByTagName('ratings_count')[0].childNodes[0].nodeValue
  return [avg_rate,rate_count]
  
def switch(bookList,loc):
    books = {}
    for book in bookList:
        books[book[loc]] = dict(book_id=book[0],isbn=book[1],author=book[3],pyear=book[4])
    
    #switcher is probably unecessary unless there is a way to abstract dict keys  
    #switcher = {
       # 0: 'id',
       # 1: 'isbn',
      #  2: 'title',        
      #  3: 'author',
      #  4: 'pyear',
    #}
    return books    
    
@app.route('/api/books/<string:book_isbn>')
def book_api(book_isbn):

    #Book information query
    book_req = Book.query.filter_by(isbn=book_isbn).first()
    
    if book_req is None:
        return jsonify(('Error: "Cannot find book ISBN."')),404
    else:
        book_ratings = PullRating(book_req.title)
        return jsonify({
            "title": book_req.title,
            "author": book_req.author,
            "pyear": book_req.pyear,
            "isbn": book_req.isbn,
            "review_count": book_ratings[1],
            "average_score": book_ratings[0]
            })
