from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # Add validations and constraints 
    @validates('name')
    def validate_name(self, key, name):
        names = [item[0] for item in db.session.query(Author.name).all()]
        if not name:
            raise ValueError('Name is required')
        elif name in names:
            raise ValueError('Name must be unique')
        return name
    
    @validates("phone_number")
    def validates_phone_number(self, key, number):
        if len(number) != 10:
            raise ValueError('Number has to be 10 digits!')
        return number

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # Add validations and constraints 
    @validates("title")
    def validate_title(self, key, title):
        clickbait = ["Won't Believe", "Secret", "Top", "Guess"]
        if not any(substring in title for substring in clickbait)
            raise ValueError("Not clickbait enough!")
        return title
    
    @validates("cpntent", "summary")
    def validates_content_summary_length(self,key,string):
        if key == "content" and len(string) < 250:
                raise ValueError("Content must be longer!")
        if key == "summary" and len(string) > 250:
                raise ValueError("Summary must be shorter!")
        return string
    
    @validates("category")
    def validates_category(self,key,category):
         ALLOWED_CATEGORIES = ["Fiction", "Non-Fication"]
         if category not in ALLOWED_CATEGORIES:
              raise ValueError("Bad category")
         return category

    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
