import json
import re
from flask import request, jsonify
from flask.views import View

from .models import Question
from ..meetups.models import Meetup
from . import *
# def get_all(meetup_id):
#     '''function to get all qustions per meetup'''
#     pass
# def get_question(question_id,meetup_id):
#     '''a fucntion to get a specific question'''
#     pass
# def post_question(meetup_id):
#     '''a func to post a question to a specific meetup'''
#     pass
# def upvote_question(question_id,meetup_id):
#     '''a function to upvote a question in a specific meetup'''
#     pass
# def downvote_question(question_id,meetup_id):
#     '''a function to downvote a question in a specific meetup'''
#     pass
class QuestionsView(View):
    '''this class defines manipulation of questions '''
    methods = ['POST','GET','DELETE','PUT']
    def dispatch_request(self):
        if self.request.method == 'POST':
            text = json.loads(request.data)['question_text']
            meetup_id = json.loads(request.data)['meetup']
            
            #validators
            if re.match('.*[a-zA-Z0-9]+.*',text) is None:
                return jsonify({'response':'Invalid question'}), 400

            question = Question.create_question(text,meetup_id)

            if question:
                return jsonify({'response':'question successfully posted'}), 201
            else:
                return jsonify({'response':'posting question failed'}), 401

        if self.request.method == 'GET':
            question_id = json.loads(request.data)['question_id']
            meetup_id = json.loads(request.data)['meetup_id']

            if question_id:
                question = Question.get_question(question_id)
                if question:
                    return jsonify({'response':question.__dict__}),200
                else:
                    return jsonify({'response':'question not found'}), 404
            if meetup_id:
                results = []
                questions = Question.get_all_questions(meetup_id)
                for q in questions:
                    obj = {
                        "question":q.question_text,
                        "date_posted":q.created_on,
                        "upvotes":q.upvotes,
                        "downvotes":q.downvotes,
                    }
                    results.append(obj)
                return jsonify({'questions for meetup {}'.format(meetup_id):results}), 200
                
                    

        if self.request.method == 'DELETE':
            pass
        if self.request.method == 'PUT':
            pass
        return super().dispatch_request()
    
questions_view = QuestionsView.as_view('questions_view')

#post a question 
questions_blueprint.add_url_rule('/questions/',view_func=questions_view,methods=['POST'])
##get all questions
questions_blueprint.add_url_rule('/questions/',view_func=questions_view,methods=['GET'])
#get specific question
questions_blueprint.add_url_rule('/questions/<string:question_id>',view_func=questions_view,methods=['GET'])
#upvote or downvote a question 
questions_blueprint.add_url_rule('/questions/<string:question_id>',view_func=questions_view,methods=['POST'])


