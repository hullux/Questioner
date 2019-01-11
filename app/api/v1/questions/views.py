from . import *
from flask.views import View
from .models import *
from ..meetups.models import meetup

def get_all(meetup_id):
    '''function to get all qustions per meetup'''
    pass
def get_question(question_id,meetup_id):
    '''a fucntion to get a specific question'''
    pass
def post_question(meetup_id):
    '''a func to post a question to a specific meetup'''
    pass
def upvote_question(question_id,meetup_id):
    '''a function to upvote a question in a specific meetup'''
    pass
def downvote_question(question_id,meetup_id):
    '''a function to downvote a question in a specific meetup'''
    pass
class Questions(View):
    '''this class defines manipulation of questions '''
    methods = ['POST','GET','DELETE','PUT']
    def dispatch_request(self):
        if self.request.method == 'POST':
            pass
        if self.request.method == 'GET':
            pass
        if self.request.method == 'DELETE':
            pass
        if self.request.method == 'PUT':
            pass
        return super().dispatch_request()
    
