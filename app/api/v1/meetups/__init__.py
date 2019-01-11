from flask import Blueprint

meetups_blueprint = Blueprint('meetups',__name__,template_folder='templates',static_folder='static', url_prefix='/api/v1/')