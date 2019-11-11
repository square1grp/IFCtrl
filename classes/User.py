import requests
import base64


# user class and it's singleton
class User:
    __instance = None
    __message = None
    __token = None
    user_data = dict(databases=dict(), config=dict(nav=[], pages=[]))

    @staticmethod
    def get_instance():
        if User.__instance is None:
            User()

        return User.__instance

    def __init__(self):
        if User.__instance is None:
            User.__instance = self

    # set user token
    def set_token(self, __token, user_data):
        self.__token = __token
        self.user_data = user_data

    # get user token
    def get_token(self):
        return self.__token

    # check if the current user is logged in
    def is_user_logged_in(self):
        return self.__token

    # user login. params: username, password
    def user_login(self, username, password):
        response = requests.post('http://138.68.51.100/api/v1.0/login/',
                                 json={'username': username, 'password': password})

        if response.status_code == 200:
            res_json = response.json()
            if res_json['is_authenticated']:
                # set token if user login is successed
                data_str = '%s : %s' % (username, password)
                token = base64.b64encode(data_str.encode('utf8'))
                self.__token = str(token, "utf8")
                self.__message = None
                self.user_data = dict(databases=res_json['user_databases'],
                                      config=res_json['user_info']['data_config'])

                return True

        # set error message if it's failed
        self.__message = 'Incorrect Username or Password'
        return False

    # get user info
    def get_user_data(self):
        return self.user_data

    # get page navigations
    def get_page_nav_items(self):
        return self.user_data['config']['nav']

    # get page items
    def get_page_items(self):
        return self.user_data['config']['pages']

    # user log out
    def user_logout(self):
        self.__token = None

    # get error message
    def get_message(self):
        return self.__message
