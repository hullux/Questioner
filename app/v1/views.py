<<<<<<< HEAD
from . import *
=======
from . import * 
>>>>>>> ft-user-signup-162981789

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
class UserSignUpView(MethodView):
    '''this class allows user to create an account'''
    template_name = '/auth/signup.html'
    def dispatch_request(self, *args, **kwargs):
        # return super().dispatch_request(*args, **kwargs)
        return render_template(self.template_name)
    def get(self):
        pass
    def post(self):
        pass

signup_view = UserSignUpView.as_view('signup_view')
login_view = UserLoginView.as_view('login_view')
home_view = HomeView.as_view('home_view')

home_blueprint.add_url_rule('/',view_func=home_view,methods=['GET'])

login_blueprint.add_url_rule(
    '/auth/login',
    view_func=login_view,
    methods=['POST','GET']
    )
signup_blueprint.add_url_rule('/auth/register/',
view_func=signup_view,
methods=['POST','GET']
)


