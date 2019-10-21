import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from server import app
from classes.User import User
import config

username = config.username if config.username else ''
password = config.password if config.password else ''

# get the current user instance
cur_user = User.get_instance()

# username input form field
username_input = dbc.FormGroup(
    [
        dbc.Label('Username', html_for='username'),
        dbc.Input(type='text', id='username',
                  placeholder='Enter username', value=username),
    ]
)

# password input form field
password_input = dbc.FormGroup(
    [
        dbc.Label('Password', html_for='password'),
        dbc.Input(type='password', id='password',
                  placeholder='Enter password', value=password)
    ]
)

# create login layout
layout = dbc.Row(
    [
        dbc.Col(
            [
                # for a login callback
                dcc.Location(id='login_url', refresh=True),
                html.H1('Log In', className='text-center'),
                dbc.Form([
                    username_input,
                    password_input,
                    dbc.Button(
                        'Submit',
                        n_clicks=0,
                        color='primary',
                        id='login-button',
                        className='float-right'
                    )
                ])
            ],
            className='col-12 col-md-6 col-lg-4 m-auto'
        )
    ],
    align='center',
    style={
        'height': '100vh'
    }
)

# callbacks for login action
@app.callback(Output('login_url', 'pathname'),
              [Input('login-button', 'n_clicks')],
              [State('username', 'value'),
               State('password', 'value')])
def user_login(n_clicks, username, password):
    if n_clicks and cur_user.user_login(username, password):
        return '/'
