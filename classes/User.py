from querymanager.intelliflux_dashboard_api_consumer import authenticateUser


# user class and it's singleton
class User:
    __instance = None
    __message = None
    user_data = dict(databases=dict(), config=dict(nav=[], pages=[]))

    @staticmethod
    def get_instance():
        if User.__instance is None:
            User()

        return User.__instance

    def __init__(self):
        if User.__instance is None:
            User.__instance = self

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

    # set user data
    def set_user_data(self, user_data):
        self.user_data = user_data

    # get user data
    def get_user_data(self):
        return self.user_data

    # get page navigations
    def get_page_nav_items(self):
        return self.user_data['user_info']['data_config']['nav']

    # get page items
    def get_page_items(self):
        return self.user_data['user_info']['data_config']['pages']

    # get error message
    def get_message(self):
        return self.__message
