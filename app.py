import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output, State
from server import app
from classes.User import User
from layouts import page, login
import config

# get the current user instance
cur_user = User.get_instance()

# create page layout
app.layout = html.Div(
    [
        # The local store will take the initial data
        # only the first time the page is loaded
        # and keep it until it is cleared.
        dcc.Store(id='local_storage', storage_type='local'),
        dcc.Input(id='is_storage_checked', type='hidden', value='No'),
        # container for the page content
        dbc.Container(id='page-content', fluid=True),
        # url management
        dcc.Location(id='page_url', refresh=False),
    ]
)


# callback to check user_token in local storage
@app.callback(Output('is_storage_checked', 'value'),
              [Input('local_storage', 'modified_timestamp')],
              [State('local_storage', 'data')])
def check_local_storage(ts, local_storage):
    if ts is None:
        PreventUpdate

    local_storage = local_storage or {'token': None}
    token = local_storage.get('token')

    if token:
        cur_user.set_token(token)

    return 'Yes'


# set token to the local storage
@app.callback(Output('local_storage', 'data'),
              [Input('page_url', 'pathname')])
def store_user_token(pathname):
    if pathname == '/logout' or not cur_user.is_user_logged_in():
        return {}
    elif pathname:
        return {'token': cur_user.get_token()}


# callbacks, show page content under correct page urls
@app.callback(Output('page-content', 'children'),
              [Input('page_url', 'pathname')])
def display_page(pathname):
    if pathname == '/logout':
        cur_user.user_logout()
        dcc.Location(pathname='/login', id='redirect_to_login')

    # if page is not login page and user is not logged in,
    # redriect to login page
    if not cur_user.is_user_logged_in():
        return login.layout
    elif pathname == '/login':
        return dcc.Location(pathname='/', id='redirect_to_login')

    # show pages
    return page.layout


# run the server
if __name__ == '__main__':
    # debug mode True/False
    # host ip ex: 127.0.0.1 (local), 0.0.0.0 (public)
    app.run_server(debug=config.dev_env, host=config.host_ip)
