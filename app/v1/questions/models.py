import uuid
import urllib
from datetime import  datetime
from ..meetups.models import Meetup


QUESTIONS = [
                {
                "question_id":"vv55",
                "created_on":datetime.now(),
                "question_text":"what is Python?",
                "upvotes":0,
                "downvotes":10,
                "meetup":'vsv354',
                }
            ]
COMMENTS = []

class Question(object):
    '''this class represents blueprint/manipulations of questions'''
    def __init__(self, *args, **kwargs):
        self.questions = QUESTIONS

    def create_question(self,text,meetup_id):
        '''a function to create a question'''
        question = {
            "question_id":uuid.uuid4(),
            "created_on":datetime.now(),
            "question_text":text,
            "upvotes":0,
            "downvotes":0,
            "meetup":meetup_id
        }

        self.questions.append(question)
        return question["question_id"]

    def get_question(self,question_id):
        '''function to fetch a specific question given the id'''    
        return [q for q in self.questions if q["question_id"]==question_id][0]
    def get_all_questions(self,meetup_id):
        '''a func to get all questions of a meetup'''

        return [q for q in self.questions if q["meetup"]==meetup_id]

    def upvote_question(self,question_id):
        '''a function to upvote a question'''
        question = self.get_question(question_id)
        question["upvotes"] += 1

        return question

    def downvote_question(self,question_id):
        ''' a function to downvote a question '''
        question = self.get_question(question_id)
        question["downvotes"] += 1

        return question
    
class Comment(object):
    '''this class defines posting of comments for a question'''
    def __init__(self, *args, **kwargs):
        self.comments = COMMENTS

    def create_comment(self,text,question_id):
        '''fucnction to make a comment to a specific question '''
        comment = {
            "comment_time":datetime.now(),
            "comment_text":text,
            "question":question_id,
        }
        self.comments.append(comment)

        return comment
    def get_all_comments(self,question_id):
        question_obj = Question()
        question = question_obj.get_question(question_id)
        comments = [c for c in self.comments if c["question"] == question["question_id"]]
        # if len(comments) == 0:
        #     res = {
        #         "message":"No comments found",
        #         "status_code":404
        #     }
        #     return res
        # else:
        return comments

