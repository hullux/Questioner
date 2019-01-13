from datetime import datetime
import uuid

USERS = []
class User(object):
    '''this class defines the manipulations of a user '''
    def __init__(self, *args, **kwargs):
        self.users = USERS
    def get_user(self):
        pass
    def create_user(self,user_id):
        pass
    def exists(self,user_id):
        pass