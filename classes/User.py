import requests


class User:
    __instance = None
    __is_user_logged_in = False

    @staticmethod
    def get_instance():
        if User.__instance == None:
            User()

        return User.__instance

    def __init__(self):
        self.__is_user_logged_in = False

        if User.__instance == None:
            User.__instance = self

    def is_user_logged_in(self):
        return self.__is_user_logged_in

    def user_login(self, username, password):
        requests.post('http://138.68.51.100:8080/rest-auth/login',
                      data={'username': username, 'password': password})
        pass
