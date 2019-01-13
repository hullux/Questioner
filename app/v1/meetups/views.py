import re
from flask.views import View, MethodView
import json
from flask import request, jsonify, Blueprint, Flask


from . import meetups_blueprint
from .models import Meetup

@meetups_blueprint.route('/meetups/',methods=['POST'])
def create_meetup():
    '''a endpoint to create a meetup record'''
    meetup_topic = request.json['topic']
    meetup_date = request.json['time']
    venue = request.json['venue']
    desc = request.json['description']
    image = request.json['image']
    tags = (request.json['tags'])
    print("meetup topic",tags)
    #validation
    if re.match('.*[a-zA-Z0-9]+.*', meetup_topic) is None:
        return jsonify({'response': 'invalid topic'}), 400
    if re.match('.*[a-zA-Z0-9]+.*', desc) is None:
        return jsonify({'response': 'invalid description'}), 400
    # if re.match('.*[a-zA-Z0-9]+.*',venue):
    #     return jsonify({'response':'invalid venue entry'})
    meetup_obj = Meetup()
    meetup = meetup_obj.create_meetup(meetup_topic,meetup_date,venue,desc,image,tags)

    if meetup:
        return jsonify({'response':'meetup created successfully'}),201
    else:
        return jsonify({'response':'meetup creation failed'}),401


@meetups_blueprint.route('/meetups/<string:meetup_id>',methods=['GET'])
def get_meetup(meetup_id):
    '''a endpoint to fetch one meetup record'''
    meetup_obj = Meetup()
    if meetup_id:
        meetup = meetup_obj.get_meetup(meetup_id)
        if meetup:
            return jsonify({'meetup':meetup}),200
        else:
            return jsonify({'response':'meetup not found'}),404

@meetups_blueprint.route('/meetups/',methods=['GET'])
def get_all_meetups():
    '''a endpoint to fetch all meetup records'''
    results = []
    meetup_obj = Meetup()
    meetups = meetup_obj.get_all_meetups()

    # return jsonify(meetups)
    if len(meetups) != 0:
        for meetup in meetups:
            obj = {
                "id":meetup["meetup_id"],
                "topic":meetup["meetup_topic"],
                "created_on":meetup ['created_on'],
                "details":meetup['meetup_details'],
                "rsvps":meetup['rsvps'],
                "date":meetup['meetup_date'],
                "venue":meetup['meetup_venue'],
                "tags":meetup['tags'],
                "images":meetup['images'],
            }
            results.append(obj)
        return jsonify({"meetups":results}),200
    else:
        return jsonify({"message":"No meetups found"}),404


@meetups_blueprint.route('/meetups/<string:meetup_id>',methods=['DELETE'])
def delete_meetup(meetup_id):
    '''a endpoint to delete a meetup'''
    meetup_obj = Meetup()
    if meetup_id:
        meetup = meetup_obj.get_meetup(meetup_id)
        meetups = meetup_obj.get_all_meetups()
        if meetup:
            meetups.pop(meetup)
            return jsonify({'message':"meetup successfully deleted"}),200
        else:
            return jsonify({'response':'meetup not found'}),404

@meetups_blueprint.route('/meetups/<string:meetup_id>',methods=['PUT'])
def rsvps_for_meetup(meetup_id):
    '''a endpoint to get all the rsvps submitted for a specific meetup'''
    meetup_obj = Meetup()
    meetup = meetup_obj.get_meetup(meetup_id)
    if meetup:
        meetup['rsvps'] += 1
        return jsonify({'message':"RSVP successfull for meetup {}".format(meetup["meetup_topic"])}), 201
    else:
        return jsonify({'message':"RSVP failed, meetup not found"}), 404

# @meetups_blueprint.route('/meetups/<string:meetup_id>',methods=['PUT'])
# def update_meetup(meetup_id):
#     meetup = Meetup.get_meetup(meetup_id)
#     if meetup:
#         pass
