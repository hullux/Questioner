import uuid
from datetime import  datetime

QUESTIONS = []
COMMENTS = []

class Question(object):
    '''this class represents manipulations of questions'''
    def __init__(self, *args, **kwargs):
        self.questions = QUESTIONS

    def create_question(self,text,meetup):
        '''a function to create a question'''
        question = {
            "question_id":uuid.uuid4(),
            "created_on":datetime.now(),
            "question_text":text,
            "meetup":meetup,
            "upvotes":0,
            "downvotes":0,
        }

        self.questions.append(question)
        return question["question_id"]

    def get_question(self,question_id):
        '''function to fetch a specific question given the id'''
        
        return [q for q in self.questions if q["id"]==question_id][0]
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
        question = Question.get_question(question_id)
        comment = {
            "comment_time":datetime.now(),
            "comment_text":text,
            "question":question["question_id"],
        }
        self.comments.append(comment)

        return comment
    def get_all_comments(self,question_id):
        question = Question.get_question(question_id)
        comments = [c for c in self.comments if c["question"] == question["question_id"]]
        if len(comments) == 0:
            res = {
                "message":"No comments found",
                "status_code":404
            }
            return res
        else:
            return comments

