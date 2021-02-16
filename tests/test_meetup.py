import unittest
import os 
import json
from app import create_app


class QuestionerTestCase(unittest.TestCase):
    '''This class defines quetioner test case'''
    def setUp(self):
        '''setting up test variables'''
        self.app = create_app(config_name='testing') 
        self.client = self.app.test_client
        self.meetups = [
            {
                'id': 0,
                'name':'Python Meetup',
                'location':'iHub',
                'time':'8:00 am'
            },
        ]
        self.questions = [
            {
                'id': 0,
                'text':'what is list comprehensions?',
            }
        ]
        self.votes = [
            {
                'value':1,
                'question':0, 
            },
            {
                'value':0,
                'question':0
            }
        ]

        #binding the app with current context
        # with self.app.app_context():
        #     pass

        # return super().setUp()

    def test_meetup_creation(self):
        '''testing meetup creation in the API -- POST request'''
        response = self.client().post('/v1/meetups/',data=self.meetups[0])
        self.assertEqual(response.status_code,201)
        self.assertIn('Python Meetup',str(response.data))


    def test_question_creation(self):
        '''testing question creation by a user in the API -- POST request'''
        response = self.client().post('/v1/meetups/0/questions/',data=self.questions[0])
        self.assertEqual(response.status_code,201)
        self.assertIn('list comprehensions',str(response.data))

    def test_one_meetup_fetch(self):
        '''test getting of a specific meetup record -- GET request'''
        response = self.client().get('/v1/meetups/0')
        self.assertIn('Python Meetup',str(response.data[0]))
    
    def test_all_meetups_fetch(self):
        '''test API can get all the meetups -- GET request'''
        response_one = self.client().get('/v1/meetups/',data=self.meetups)
        response_two = self.client().get('/v1/meetups/')
        self.assertEqual(response_one.status_code,201)
        self.assertEqual(response_two.status_code,200)
        self.assertIn('iHub',str(response_two.data[0]))

    def test_upvote_downvote(self):
        '''test upvote or downvote on a question'''
        response_upvote = self.client().post('/v1/meetups/',data=self.votes[0])
        response_downvote =self.client().post('/v1/meetups/',data=self.votes[1])
        self.assertEqual(response_upvote.status_code,201)
        self.assertEqual(response_downvote.status_code,201)
        self.assertIn('1',str(response_upvote.data[0]))
        self.assertIn('0',str(response_upvote.data[1]))
    
    def tearDown(self):
        pass
        # with self.app.app_context():

        # return super().tearDown()
if __name__ == "__main__":
    unittest.main()