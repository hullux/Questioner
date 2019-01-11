from . import *
from .models import *

from flask.views import View


class Meetups(View):
    '''this class defines all the manipulations for meetups'''
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