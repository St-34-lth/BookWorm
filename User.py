class User:

    def __init__(self,uname,pwd):

        self.name = uname
        self.pwd = pwd 
        self.books = []

    def __repr__(self):
        return self.name 


