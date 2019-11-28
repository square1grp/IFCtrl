from querymanager.intelliflux_dashboard_api_consumer import authenticateUser
from datetime import datetime, timedelta
import json
import base64

user_data = None

with open('user_data.json', 'r') as f:
    user_data = json.loads(f.read())


# user class and it's singleton
class User:
    __instance = None
    __message = dict(form=None, username=None, password=None)
    __auth = dict(username=None, password=None)
    username = None
    token = None
    user_data = None
    database_id = None
    time_stamp_from = None
    time_stamp_to = None

    @staticmethod
    def get_instance():
        if User.__instance is None:
            User()

        return User.__instance

    def __init__(self):
        if User.__instance is None:
            User.__instance = self

    # set user token
    def set_token(self, token):
        self.token = token

        if self.user_data is None:
            self.load_user_data_cache()

    # get user token
    def get_token(self):
        return self.token

    # get user name
    def get_username(self):
        if self.token is not None:
            self.username = base64.b64decode(self.token).decode()

        return self.username

    # user login. params: username, password
    def user_login(self, username, password):
        user_data = authenticateUser(username, password)

        if user_data is not None:
            if user_data['is_authenticated']:
                # set error message if it's failed
                self.set_message(dict(
                    form=None,
                    username=None,
                    password=None
                ))

                self.user_data = user_data

                token = base64.b64encode(username.encode()).decode()
                self.set_token(token)

                self.save_user_data_cache()

                return True

        # set error message if it's failed
        self.set_message(dict(
            form='Username or Password is incorrect.',
            username=None,
            password=None
        ))
        return False

    # set auth
    def set_auth(self, username, password):
        self.__auth = dict(username=username, password=password)

    # get auth
    def get_auth(self):
        return self.__auth

    # get user data
    def get_user_data(self):
        return self.user_data

    # set user data
    def set_user_data(self, user_data):
        self.user_data = user_data
        self.database_id = 1
        self.time_stamp_from = self.get_time_stamp_yesterday()
        self.time_stamp_to = self.get_time_stamp_today()

    # load user_data cache
    def load_user_data_cache(self):
        self.user_data = None

        if self.token:
            try:
                with open('user_data_temp/%s.json' % self.token, 'r') as f:
                    self.user_data = json.loads(f.read())
            except:
                pass

        return self.user_data

    # save user_data cache
    def save_user_data_cache(self):
        if self.token:
            try:
                with open('user_data_temp/%s.json' % self.token, 'w') as f:
                    f.write(json.dumps(self.user_data))
            except:
                pass

    # get page navigations
    def get_page_nav_items(self):
        return self.user_data['user_info']['data_config']['nav']

    # get page items
    def get_page_items(self):
        return self.user_data['user_info']['data_config']['pages']

    # set error message, field=username, password
    def set_message(self, message):
        self.__message = message

    # get error message
    def get_message(self):
        return self.__message

    # get user id
    def get_user_id(self):
        return self.user_data['user_info']['id']

    # get user databases
    def get_user_databases(self):
        if self.user_data['user_databases']:
            return self.user_data['user_databases'].values()
        else:
            return []

    # get current user database id
    def get_user_database_id(self):
        return self.database_id

    # set current user database id
    def set_user_database_id(self, database_id):
        self.database_id = database_id

    # get time stamp yeaterday
    def get_time_stamp_yesterday(self):
        return (datetime.today() - timedelta(days=1)).strftime('%Y-%m-%d')

    # get time stamp today
    def get_time_stamp_today(self):
        return datetime.today().strftime('%Y-%m-%d')

    # get time stamp from
    def get_time_stamp_from(self):
        return self.time_stamp_from

    # set time stamp from
    def set_time_stamp_from(self, time_stamp_from=None):
        self.time_stamp_from = time_stamp_from if time_stamp_from else self.get_time_stamp_yesterday()

    # get time stamp to
    def get_time_stamp_to(self):
        return self.time_stamp_to

    # set time stamp to
    def set_time_stamp_to(self, time_stamp_to=None):
        self.time_stamp_to = time_stamp_to if time_stamp_to else self.get_time_stamp_today()
