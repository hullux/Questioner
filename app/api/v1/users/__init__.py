from flask import Blueprint

#login blueprint 
login_blueprint = Blueprint(
                    'login',
                    __name__,
                    template_folder='templates',
                    static_folder='static',
                    url_prefix='/auth/'
                    )
#signup blueprint
signup_blueprint = Blueprint(
                    'signup',
                    __name__,
                    template_folder='templates',
                    static_folder='static',
                    url_prefix='/auth/'
                    )
#home blueprint
home_blueprint = Blueprint(
                    'home',
                    __name__,
                    template_folder='templates',
                    static_folder='static'
                    )
