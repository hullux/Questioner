from . import *

from flask.views import View 
from flask import make_response, request, jsonify, render_template

class HomeView(View):
    '''this is the index page view'''
    methods = ['GET','POST']
    template_name = '/user/index.html'
    def dispatch_request(self, *args, **kwargs):
        return render_template(self.template_name)
    
class UserLoginView(View):
    '''this class allows a user to log into the platform'''
    methods = ['GET','POST']
    template_name = '/auth/login.html'
    def dispatch_request(self, *args, **kwargs):
        # return super().dispatch_request(*args, **kwargs)
        return render_template(self.template_name)
    

class UserSignUpView(View):
    '''this class allows user to create an account'''
    methods = ['GET','POST']
    template_name = '/auth/signup.html'
    def dispatch_request(self, *args, **kwargs):
        # return super().dispatch_request(*args, **kwargs)
        return render_template(self.template_name)
    

home_blueprint.add_url_rule('/',view_func=HomeView.as_view('home_view'))
login_blueprint.add_url_rule('/auth/login',view_func=UserLoginView.as_view('login_view'))
signup_blueprint.add_url_rule('/auth/register/',view_func=UserSignUpView.as_view('signup_view'))


