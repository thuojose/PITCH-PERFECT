import unittest
from app.models import Pitch, Comment,User
from app import db

class TestPitch(unittest.TestCase):
    '''
    A test case that tests the behaviours of the Pitch model
    '''

    def setUp(self):
        '''
        Method that will run before each test is ran
        '''
        self.new_pitch = Pitch(pitch_content = "Amazing pitch", pitch_category = 'Business')
        self.new_comment = Comment(comment_content = "I love this", pitch=self.new_pitch)


    def tearDown(self):
        db.session.delete(self)
        User.query.commit()


    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment, Comment))


    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment, Comment, "I love this")
        self.assertEquals(self.new_comment.pitch, self.new_pitch, "Amazing pitch")