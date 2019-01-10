from . import *

from flask.views import MethodView 
from flask import make_response, request, jsonify, render_template
class HomeView(MethodView):
    '''this is the index page view'''
    template_name = '/user/index.html'
    def dispatch_request(self, *args, **kwargs):
        return render_template(self.template_name)
    def get(self):
        pass

class UserLoginView(MethodView):
    '''this class allows a user to log into the platform'''
    template_name = '/auth/login.html'
    def dispatch_request(self, *args, **kwargs):
        # return super().dispatch_request(*args, **kwargs)
        return render_template(self.template_name)
    def post(self):
        '''this method handles user login ---> /auth/login'''
        return "user login"
    def get(self):
        '''this method handles user login ---> /auth/login'''
        # return super(UserLoginView,self)
        return "user login"

login_view = UserLoginView.as_view('login_view')
home_view = HomeView.as_view('home_view')

home_blueprint.add_url_rule('/',view_func=home_view,methods=['GET'])

login_blueprint.add_url_rule(
    '/auth/login',
    view_func=login_view,
    methods=['POST','GET']
    )

