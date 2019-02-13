# from datetime import datetime, timedelta
import unittest
from .app import *
from app.models import User, Pitch

class UserModelCase(unittest.TestCase):
    def setUp(self):
        self.user_evans = User(id=1,username = 'evans',password = 'gerraut', email = 'mudavadie@gmail.com')

    def tearDown(self):
        User.query.delete()
    def test_password_hashing(self):
        u = User(username='edgar')
        u.set_password('1234')
        self.assertFalse(u.check_password('pass123'))
        self.assertTrue(u.check_password('1234'))
    def test_save_user(self):

        def test_check_instance_variables(self):
            self.assertEquals(self.user_James.username,'evans')
            self.assertEquals(self.user_James.password,'gerraut')
            self.assertEquals(self.user_James.email,"mudavadie@gmail.com")
    def test_save_review(self):
        self.user_evans.save_user()
        self.assertTrue(len(User.query.all())>0)
    def test_get_user_by_id(self):
        self.user_evans.save_user()
        fetched_user = User.get_user(1)
        self.assertTrue(len(fetched_user) == 1)
