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
    token = None
    user_data_list = dict()
    database_id_list = dict()
    time_stamp_from_list = dict()
    time_stamp_to_list = dict()

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
        username = self.get_username()

        if username is not None:
            self.set_user_data(username, self.load_user_data_cache())

    # get user token
    def get_token(self):
        return self.token

    # get user name
    def get_username(self):
        if self.get_token() is not None:
            return base64.b64decode(self.get_token()).decode()

        return None

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

                self.set_user_data(username, user_data)
                token = base64.b64encode(username.encode()).decode()
                self.set_token(token)

                self.save_user_data_cache(user_data)

                return True

        # set error message if it's failed
        self.set_message(dict(
            form='Username or Password is incorrect.',
            username=None,
            password=None
        ))
        return False

    # get user data
    def get_user_data(self):
        username = self.get_username()

        if username is not None:
            return self.user_data_list[username]

        return dict()

    # set user data
    def set_user_data(self, username=None, user_data=[]):
        if username is None:
            return

        self.user_data_list[username] = user_data
        db = [db for db in user_data['user_databases'].values()][0]
        self.database_id_list[username] = db['user_database_id']
        self.time_stamp_from_list[username] = self.get_time_stamp_yesterday()
        self.time_stamp_to_list[username] = self.get_time_stamp_today()

    # load user_data cache
    def load_user_data_cache(self):
        try:
            with open('user_data_temp/%s.json' % self.get_token(), 'r') as f:
                return json.loads(f.read())
        except:
            return []

    # save user_data cache
    def save_user_data_cache(self, user_data):
        try:
            with open('user_data_temp/%s.json' % self.get_token(), 'w') as f:
                f.write(json.dumps(user_data))
        except:
            pass

    # get page navigations
    def get_page_nav_items(self):
        try:
            user_data = self.get_user_data()

            return user_data['user_info']['data_config']['nav']
        except:
            return []

    # get page items
    def get_page_items(self):
        try:
            user_data = self.get_user_data()

            return user_data['user_info']['data_config']['pages']
        except:
            return []

    # set error message, field=username, password
    def set_message(self, message):
        self.__message = message

    # get error message
    def get_message(self):
        return self.__message

    # get user id
    def get_user_id(self):
        try:
            user_data = self.get_user_data()

            return user_data['user_info']['id']
        except:
            return None

    # get user databases
    def get_user_databases(self):
        try:
            user_data = self.get_user_data()

            return user_data['user_databases'].values()
        except:
            return []

    # get current user database id
    def get_user_database_id(self):
        username = self.get_username()

        if username is not None:
            return self.database_id_list[username]

        return None

    # set current user database id
    def set_user_database_id(self, database_id):
        username = self.get_username()

        if username is not None:
            self.database_id_list[username] = database_id

    # get time stamp yeaterday
    def get_time_stamp_yesterday(self):
        return (datetime.today() - timedelta(days=1)).strftime('%Y-%m-%d')

    # get time stamp today
    def get_time_stamp_today(self):
        return datetime.today().strftime('%Y-%m-%d')

    # get time stamp from
    def get_time_stamp_from(self):
        username = self.get_username()

        if username is not None:
            return self.time_stamp_from_list[username]

        return self.get_time_stamp_yesterday()

    # set time stamp from
    def set_time_stamp_from(self, time_stamp_from=None):
        username = self.get_username()

        if username is not None:
            self.time_stamp_from_list[username] = time_stamp_from if time_stamp_from else self.get_time_stamp_yesterday(
            )

    # get time stamp to
    def get_time_stamp_to(self):
        username = self.get_username()

        if username is not None:
            return self.time_stamp_to_list[username]

        return self.get_time_stamp_today()

    # set time stamp to
    def set_time_stamp_to(self, time_stamp_to=None):
        username = self.get_username()

        if username is not None:
            self.time_stamp_to_list[username] = time_stamp_to if time_stamp_to else self.get_time_stamp_today()
