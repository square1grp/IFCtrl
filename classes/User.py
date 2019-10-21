import requests


# user class and it's singleton
class User:
    __instance = None
    __message = None
    __token = None

    @staticmethod
    def get_instance():
        if User.__instance == None:
            User()

        return User.__instance

    def __init__(self):
        if User.__instance == None:
            User.__instance = self

    # set user token
    def set_token(self, __token):
        self.__token = __token

    # get user token
    def get_token(self):
        return self.__token

    # check if the current user is logged in
    def is_user_logged_in(self):
        return self.__token

    # user login. params: username, password
    def user_login(self, username, password):
        response = requests.post('http://138.68.51.100:8080/rest-auth/login/',
                                 data={'username': username, 'password': password})

        if response.status_code == 200:
            # set token if user login is successed
            self.__token = response.json()['key']
            self.__message = None

            return True
        else:
            # set error message if it's failed
            self.__message = 'Incorrect Username or Password'
            return False

    # user log out
    def user_logout(self):
        self.__token = None

    # get error message
    def get_message(self):
        return self.__message
