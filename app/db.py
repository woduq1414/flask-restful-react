from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

db = SQLAlchemy()


class User(db.Model):
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    userSeq = db.Column(db.Integer, primary_key=True, nullable=False)
    id = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    nickname = db.Column(db.String(20), nullable=False)