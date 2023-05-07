from flask import current_app
from flask_testing import TestCase
from app import create_app, db
from app.db.models import User


class UserModelTestCase(TestCase):
    def create_app(self):
        app = create_app()
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        app.config['TESTING'] = True
        return app
    
    def setUp(self):
        self.app = self.create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        
            
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
            
    def test_create_user(self):
        user = User(first_name='James',last_name='Jones',email='james_jones@mail.com',hashed_password='password',status="Online")
        with self.app_context():
            db.session.add(user)
            db.session.commit()

        saved_user = User.query.filter_by(email='james_jones@mail.com').first()
        self.assertEqual(saved_user.first_name, 'James')
        self.assertEqual(saved_user.last_name, 'Jones')
        self.assertEqual(saved_user.status, 'Online')
    
    def test_delete_user(self):
        user = User(first_name='Jane',last_name='Smith',email='jane_smith@mail.com',hashed_password='password',status="Online")
        with self.app_context():
            db.session.add(user)
            db.session.commit()
            
            db.session.delete(user)
            db.session.commit()
        
        
        deleted_user =  User.query.filter_by(email='jane_smith@mail.com').first()
        self.assertIsNone(deleted_user)
        
