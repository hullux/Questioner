
from flask import Blueprint, render_template, abort, request, make_response, jsonify
from jinja2 import TemplateNotFound
from flask.views import MethodView
from . import *

#creating blueprints here 

# simple_page = Blueprint('simple_page',__name__,url_prefix='/api/v1/')
# home_blueprint = Blueprint('home',__name__,url_prefix='/api/v1/')
# login_blueprint = Blueprint('login',__name__,url_prefix='/api/v1/')
# signup_blueprint = Blueprint('signup',__name__,url_prefix='/api/v1/')

# class HomeView(MethodView):
#     '''this is the index page view'''
#     template_name = '/user/index.html'
#     methods=['GET','POST']
#     def dispatch_request(self, *args, **kwargs):
#         if request.method == 'GET':
#             return render_template(self.template_name)
#     # def get(self):
#     #     return render_template(self.template_name)
# @home_blueprint.route('',methods=['GET'])
# def home_view():
#     template_name = '/user/index.html'
#     return render_template(template_name)




# class UserLoginView(MethodView):
#     '''this class allows a user to log into the platform'''
#     template_name = '/auth/login.html'
#     methods=['POST']
#     def dispatch_request(self, *args, **kwargs):
#         if request.method == 'POST':
#             return render_template(self.template_name)
#     # def post(self):
#     #     return render_template(self.template_name)

# @login_blueprint.route('/auth/login',methods=['POST'])
# def login_view():
#     template_name = '/auth/login.html'
#     if request.method == 'POST':
#         return render_template(template_name)
#     else:
#         return {"message":'method not allowed',"status_code":404}

# class UserSignUpView(MethodView):
#     '''this class allows user to create an account'''
#     template_name = '/auth/signup.html'
#     methods=['POST']
#     def dispatch_request(self, *args, **kwargs):
#         if request.method == 'POST':
#             return render_template(self.template_name)
#     # def post(self):
#     #     return render_template(self.template_name)
# @signup_blueprint.route('/auth/register',methods=['POST'])
# def signup_view():
#     template_name = '/auth/signup.html'
#     if request.method == 'POST':
#         return render_template(template_name)
#     else:
#         return {"message":'method not allowed',"status_code":404}

@simple_page.route('/', defaults={'page': 'index'},methods=['GET'])
@simple_page.route('/<page>',methods=['GET','POST'])
def show(page):
    try:
        return render_template('/user/index.html')
    except TemplateNotFound:
        abort(404)

@signup_blueprint.route('/auth/register',methods=['POST'])
def signup_view():
    template_name = '/auth/signup.html'
    if request.method == 'POST':
        return render_template(template_name)
    else:
        return {"message":'method not allowed',"status_code":404}

@login_blueprint.route('/auth/login',methods=['POST'])
def login_view():
    template_name = '/auth/login.html'
    if request.method == 'POST':
        return render_template(template_name)
    else:
        return {"message":'method not allowed',"status_code":404}

@home_blueprint.route('/home',methods=['GET'])
def home_view():
    template_name = '/user/index.html'
    return render_template(template_name)


# class TestMe(MethodView):
#     template_name = '/user/index.html'
#     methods=['GET']
#     def dispatch_request(self, *args, **kwargs):
#         if request.method == 'GET':
#             return render_template(self.template_name)
#         # return super().dispatch_request(*args, **kwargs)


# test_view = TestMe.as_view('testing')
# home_view = HomeView.as_view('home')
# login_view = UserLoginView.as_view('login')
# signup_view = UserSignUpView.as_view('signup')

# home_blueprint.add_url_rule('/home',view_func=home_view)
# login_blueprint.add_url_rule('/auth/login',view_func=login_view)
# signup_blueprint.add_url_rule('/auth/register/',view_func=signup_view)


# simple_page.add_url_rule('',view_func=test_view)