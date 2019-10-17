import requests


class User:
    __instance = None

    __token = None

    @staticmethod
    def get_instance():
        if User.__instance == None:
            User()

        return User.__instance

    def __init__(self):
        if User.__instance == None:
            User.__instance = self

    def is_user_logged_in(self):
        return self.__token

    def user_login(self, username, password):
        response = requests.post('http://138.68.51.100:8080/rest-auth/login/',
                      data={'username': username, 'password': password})
        
        if response.status_code == 200:
            self.__token = response.json()['key']

            return True
        else:
            return False

    def user_logout(self):
        self.__token = None