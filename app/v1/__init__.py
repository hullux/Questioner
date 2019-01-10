from flask import Blueprint

#login blueprint 
login_blueprint = Blueprint('login',__name__)
signup_blueprint = Blueprint('signup',__name__)
create_meetup_blueprint = Blueprint('create_meetup',__name__)
create_question_blueprint = Blueprint('create_question',__name__)
upvote_downvote_blueprint = Blueprint('upvote_downvote',__name__)
rsvp_blueprint = Blueprint('rsvp',__name__)
get_meetups = Blueprint('get_meetups',__name__)
home_blueprint = Blueprint('home',__name__)


from . import views