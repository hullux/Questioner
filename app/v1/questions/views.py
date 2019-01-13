import json
import re
from flask import request, jsonify
from flask.views import View

from .models import Question
from ..meetups.models import Meetup
from . import *

@questions_blueprint.route('/questions/',methods=['POST'])
def create_question(meetup_id):
    '''this endpoint provides the functionality of creating a question'''
    text = request.json['question_text']
    question_obj = Question()

    #validators
    if re.match('.*[a-zA-Z0-9]+.*',text) is None:
        return jsonify({'response':'Invalid question'}), 400

    question = question_obj.create_question(text)

    if question:
        return jsonify({'response':'question successfully posted'}), 201
    else:
        return jsonify({'response':'posting question failed'}), 401


@questions_blueprint.route('/questions/all/<string:meetup_id>',methods=['GET'])
def get_questions(meetup_id):
    '''
    this endpoint provides the functionality of 
    fetching all questions for a pecific meetup.
    '''
    meetup_obj = Meetup()
    meetup = meetup_obj.get_meetup(meetup_id)
    # print("meetup",meetup)
    results = []
    question_obj = Question()
    questions = question_obj.get_all_questions(meetup_id)
    if len(questions) >= 1:
        for q in questions:
            obj = {
                "question_id":q["question_id"],
                "question":q['question_text'],
                "date posted":q['created_on'],
                "upvotes":q['upvotes'],
                "downvotes":q['downvotes'],
            }
            results.append(obj)
        return jsonify({'questions for meetup {}'.format(meetup["meetup_topic"]):results}), 200
    else:
        return jsonify({"message":"No questions found for {}".format(meetup["meetup_topic"])}),404

@questions_blueprint.route('/questions/<string:question_id>',methods=['GET'])
def get_question(question_id):
    '''this endpoint provides the functionality of fetching on question'''
    question_obj = Question()
    question = question_obj.get_question(question_id)
    if question:
        return jsonify({'response':question}),200
    else:
        return jsonify({'response':'question not found'}), 404

@questions_blueprint.route('/questions/<string:question_id>/upvote',methods=['PUT'])
def upvote_question(question_id):
    '''this endpoint provides a functionality to upvote a question'''
    question_obj = Question()
    question = question_obj.get_question(question_id)
    if question:
        question["upvotes"] += 1
        return jsonify({"message":"Upvote successfull"}), 201
    else:
        return jsonify({"message":"Upvote successfull.Question not found"}), 404

@questions_blueprint.route('/questions/<string:question_id>/downvote',methods=['PUT'])
def downvote_question(question_id):
    '''this endpoint provides the fucntionality to downvote a question'''
    question_obj = Question()
    question = question_obj.get_question(question_id)
    if question:
        question["downvotes"] += 1
        return jsonify({"message":"Downvote successfull"}), 201
    else:
        return jsonify({"message":"Downvote successfull.Question not found"}), 404
