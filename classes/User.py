from querymanager.intelliflux_dashboard_api_consumer import authenticateUser
from datetime import datetime


# user class and it's singleton
class User:
    __instance = None
    __message = None
    user_data = dict(databases=dict(), config=dict(nav=[], pages=[]))
    database_id = 4
    time_stamp_from = '2019-10-01'
    time_stamp_to = '2019-10-02'

    @staticmethod
    def get_instance():
        if User.__instance is None:
            User()

        return User.__instance

    def __init__(self):
        if User.__instance is None:
            User.__instance = self

    # user login. params: username, password
    def user_login(self, username, password):
        user_data = authenticateUser(username, password)

        if user_data is not None:
            if user_data['is_authenticated']:
                self.__message = None
                self.user_data = user_data

                return True

        # set error message if it's failed
        self.__message = 'Incorrect Username or Password'
        return False

    # get user data
    def get_user_data(self):
        return self.user_data

    # set user data
    def set_user_data(self, user_data):
        self.user_data = user_data

    # get page navigations
    def get_page_nav_items(self):
        return self.user_data['user_info']['data_config']['nav']

    # get page items
    def get_page_items(self):
        return self.user_data['user_info']['data_config']['pages']

    # get error message
    def get_message(self):
        return self.__message

    # get user id

    def get_user_id(self):
        return self.user_data['user_info']['id']

    # get user name
    def get_user_name(self):
        return 'ifadmin'

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

    # get time stamp now
    def get_time_stamp_now(self):
        return datetime.now().strftime('%Y-%m-%d')

    # get time stamp from
    def get_time_stamp_from(self):
        return self.time_stamp_from

    # set time stamp from
    def set_time_stamp_from(self, time_stamp_from=None):
        self.time_stamp_from = time_stamp_from if time_stamp_from else self.get_time_stamp_now()

    # get time stamp to
    def get_time_stamp_to(self):
        return self.time_stamp_to

    # set time stamp to
    def set_time_stamp_to(self, time_stamp_to=None):
        self.time_stamp_from = time_stamp_to if time_stamp_to else self.get_time_stamp_now()
