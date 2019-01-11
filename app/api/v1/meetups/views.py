from flask.views import View
import json
from flask import request, jsonify
import re

from . import *
from .models import Meetup

class MeetupsView(View):
    '''this class defines all the manipulations for meetups'''
    methods = ['POST','GET','DELETE','PUT']
    def dispatch_request(self):
        if self.request.method == 'POST':
            meetup_topic = json.loads(request.data)['topic']
            meetup_date = json.loads(request.data)['time']
            venue = json.loads(request.data)['venue']
            desc = json.loads(request.data)['description']
            image = json.loads(request.data)['image']
            tags = json.loads(request.data)['tags']

            #validation
            if re.match('.*[a-zA-Z0-9]+.*', meetup_topic) is None:
                return jsonify({'response': 'invalid topic'}), 400
            if re.match('.*[a-zA-Z0-9]+.*', desc) is None:
                return jsonify({'response': 'invalid description'}), 400
            # if re.match('.*[a-zA-Z0-9]+.*',venue):
            #     return jsonify({'response':'invalid venue entry'})
            
            meetup = Meetup.create_meetup(meetup_topic,meetup_date,venue,desc,image,tags)

            if meetup:
                return jsonify({'response':'meetup created successfully'}),201
            else:
                return jsonify({'response':'meetup creation failed'}),401

        if self.request.method == 'GET':
            meetup_id = json.loads(request.data)["meetup_id"]
            if meetup_id:
                meetup = Meetup.get_meetup(meetup_id)
                if meetup:
                    return jsonify({'meetup':meetup.__dict__}),200
                else:
                    return jsonify({'response':'meetup not found'}),404
            else:
                results = []
                meetups = Meetup.get_all_meetups()

                for meetup in meetups:
                    obj = {
                        "id":meetup.meetup_id,
                        "topic":meetup.meetup_topic,
                        "created_on":meetup.created_on,
                        "details":meetup_details,
                        "rsvps":meetup.rsvps,
                        "date":meetup.meetup_date,
                        "venue":meetup.meetup_venue,
                        "tags":meetup.tags,
                        "images":meetup.images,
                    }
                    results.append(obj)
                    
                return jsonify({"meetups":results}),200

        if self.request.method == 'DELETE':
            pass
        if self.request.method == 'PUT':
            pass
        return super().dispatch_request()

meetup_view = MeetupsView.as_view('meetups')

meetups_blueprint.add_url_rule('/meetups/',view_func=meetup_view,methods=['GET'])
meetups_blueprint.add_url_rule('/meetups/<string:meetup_id>',view_func=meetup_view,methods=['GET'])
meetups_blueprint.add_url_rule('/meetups/',view_func=meetup_view,methods=['POST'])
meetups_blueprint.add_url_rule('/meetups/<string:meetup_id>',view_func=meetup_view,methods=['DELETE'])
meetups_blueprint.add_url_rule('/meetups/<string:meetup_id>',view_func=meetup_view,methods=['PUT'])
