from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

from database import Base, db_session, init_db


class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)
    title = Column(String(120), unique=True, nullable=False)
    content = Column(Text)
    date_posted = Column(DateTime, default=datetime.utcnow())

    user_id = Column(Integer, ForeignKey('user.id'))

    def __repr__(self):
        return "<Post(id='{}', title='{}')>".format(self.id, self.title)


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    profile_image = Column(String(100), default='default.png')

    posts = relationship('Post', backref='author', lazy=True)

    def __init__(self, username, email, password, **kwargs):
        self.username = username
        self.email = email

        self.set_password(password)

    def __repr__(self):
        return "<User(id='{}', username='{}', email='{}')>".format(self.id, self.username, self.email)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

init_db()

if __name__ == '__main__':
    breakpoint()

