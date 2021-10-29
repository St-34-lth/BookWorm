<<<<<<< HEAD
import csv
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from Models import Book 
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import os
path = os.path.abspath(r"C:\Users\M\Desktop\Web app\project1\books.csv")



app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://jscgdcozzllrcb:f9d3040fa55f18c09257c63af9f0568887f5b4ee9c12adde26fe189743412f26@ec2-46-137-177-160.eu-west-1.compute.amazonaws.com:5432/d72lps0f3so6mt'
app.config["DATABASE_URL"] = 'postgres://jscgdcozzllrcb:f9d3040fa55f18c09257c63af9f0568887f5b4ee9c12adde26fe189743412f26@ec2-46-137-177-160.eu-west-1.compute.amazonaws.com:5432/d72lps0f3so6mt'

db = SQLAlchemy(app)



def main():

        with open(path,'r') as f:
            reader = csv.reader(f,delimiter=',')


        
            for isbn,title,author,pyear in reader:
                if not isbn=='isbn':
                    
                    book =Book(isbn=str(isbn),title=title,author=author,pyear=pyear)
                    db.session.add(book)
                db.session.commit()
                #else:
                # pass
            


if __name__ == "__main__":
    main()

 

=======
import csv
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from Models import Book 
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import os
path = os.path.abspath(r"C:\Users\M\Desktop\Web app\project1\books.csv")



app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://jscgdcozzllrcb:f9d3040fa55f18c09257c63af9f0568887f5b4ee9c12adde26fe189743412f26@ec2-46-137-177-160.eu-west-1.compute.amazonaws.com:5432/d72lps0f3so6mt'
app.config["DATABASE_URL"] = 'postgres://jscgdcozzllrcb:f9d3040fa55f18c09257c63af9f0568887f5b4ee9c12adde26fe189743412f26@ec2-46-137-177-160.eu-west-1.compute.amazonaws.com:5432/d72lps0f3so6mt'

db = SQLAlchemy(app)



def main():

        with open(path,'r') as f:
            reader = csv.reader(f,delimiter=',')


        
            for isbn,title,author,pyear in reader:
                if not isbn=='isbn':
                    
                    book =Book(isbn=str(isbn),title=title,author=author,pyear=pyear)
                    db.session.add(book)
                db.session.commit()
                #else:
                # pass
            


if __name__ == "__main__":
    main()

 

>>>>>>> e91c249518180045abfd580520895a5a4e9f2171
