"""
IntelliFlux Dashboard API Consumer
-------------
This class conist of all mthods for getting data from IntelliFlux Dashboard API

"""

import requests
import json
from requests.auth import HTTPBasicAuth


# This method consume the API method for user authentication and provide user databases list and dashboard widgets configurations
def authenticateUser(username, password):
    try:
        # Request paramaters for Intelliflux Dashboard API
        params = {'username': username, 'password': password}
        # Requesting API login method to authenticate user and getting his Databases and Dashboard Configurations
        headers = {'content-type': 'application/json'}
        # Please load url from config file of your dash app
        api_response = requests.post(
            'http://138.68.51.100/api/v1.0/login/', headers=headers, data=json.dumps(params)
        )
        user_data = json.loads(api_response.text)
        return user_data
    except (Exception) as error:
        print(error)
    return None

# This method consume the API method to execute a generic query against specified database


def getWidgetData(database_id, sqlquery):
    try:
        # Request paramaters for Intelliflux Dashboard API
        params = {'database_id': database_id, 'sqlquery': sqlquery}
        # Requesting API Execute a query for a sepcific Databases to get Widget Data which dose not exist in cache
        headers = {'content-type': 'application/json'}
        # Please load url from config file of your dash app
        api_response = requests.get(
            'http://138.68.51.100/api/v1.0/dashboarddata/', headers=headers, data=json.dumps(params), auth=HTTPBasicAuth('admin', 'admin@123')
        )
        return api_response.text
        widget_data = json.loads(api_response.text)
        return widget_data
    except (Exception) as error:
        print(error)
    return None


# This method consume the API method to create new user
def createUser(username, password, confirm_password, data_config):
    try:
        # Request paramaters for Intelliflux Dashboard API
        params = {'username': username, 'password': password,
                  'confirm_password': confirm_password, 'data_config': data_config}
        # Requesting API to Execute a query for a sepcific Databases in order to get Widget Data which dose not exist in cache
        headers = {'content-type': 'application/json'}
        # Please load url from config file of your dash app
        api_response = requests.post(
            'http://138.68.51.100/api/v1.0/createuser/', headers=headers, data=json.dumps(params), auth=HTTPBasicAuth('admin', 'admin@123')
        )
        widget_data = json.loads(api_response.text)
        return widget_data
    except (Exception) as error:
        print(error)
    return None
