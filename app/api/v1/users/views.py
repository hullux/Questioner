from . import *

from flask.views import View,MethodView
from flask import make_response, request, jsonify, render_template

class HomeView(MethodView):
    '''this is the index page view'''
    template_name = '/user/index.html'
    def dispatch_request(self, *args, **kwargs):
        return render_template(self.template_name)
    def get(self):
        return "home"
    
class UserLoginView(MethodView):
    '''this class allows a user to log into the platform'''
    template_name = '/auth/login.html'
    def dispatch_request(self, *args, **kwargs):
        # return super().dispatch_request(*args, **kwargs)
        return render_template(self.template_name)
    def post(self):
        return "user login"
    

class UserSignUpView(MethodView):
    '''this class allows user to create an account'''
    template_name = '/auth/signup.html'
    def dispatch_request(self, *args, **kwargs):
        # return super().dispatch_request(*args, **kwargs)
        return render_template(self.template_name)
    def post(self):
        return "user sign up"
    
home_view = HomeView.as_view('home_view')
login_view = UserLoginView.as_view('login_view')
signup_view = UserSignUpView.as_view('signup_view')

home_blueprint.add_url_rule('/',view_func=home_view,methods=['GET'])
login_blueprint.add_url_rule('/auth/login',view_func=login_view,methods=['POST'])
signup_blueprint.add_url_rule('/auth/register/',view_func=signup_view,methods=['POST'])


