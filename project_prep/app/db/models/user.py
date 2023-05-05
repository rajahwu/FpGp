from datetime import datetime
from ..dev import db


class User(db.Model):
    __tablename__ = "users"
    # Table Keys
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    hashed_password = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(255), nullable=False)
    
    # Common Keys
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False, defalut=datetime.now())
    updated_at = db.Column(db.DateTime, nullable=False, defalut=datetime.now())