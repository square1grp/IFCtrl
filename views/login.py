import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from server import app
from classes.User import User
import config

username = config.username if config.username else ''
password = config.password if config.password else ''

cur_user = User.get_instance()

username_input = dbc.FormGroup(
    [
        dbc.Label('Username', html_for='username'),
        dbc.Input(type='text', id='username',
                  placeholder='Enter username', value=username),
    ]
)

password_input = dbc.FormGroup(
    [
        dbc.Label('Password', html_for='password'),
        dbc.Input(type='password', id='password',
                  placeholder='Enter password', value=password)
    ]
)

layout = dbc.Row(
    [
        dbc.Col(
            [
                dcc.Location(id='login_url', refresh=True),
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
                ]),
                html.Div(children='', id='output-state'),
            ],
            className='col-12 col-md-6 col-lg-4 m-auto'
        )
    ],
    align='center',
    style={
        'height': '100vh'
    }
)


@app.callback(Output('login_url', 'pathname'),
              [Input('login-button', 'n_clicks')],
              [State('username', 'value'),
               State('password', 'value')])
def user_login(n_clicks, username, password):
    if cur_user.user_login(username, password):
        return '/dashboard'


@app.callback(Output('output-state', 'children'),
              [Input('login-button', 'n_clicks')])
def update_output(n_clicks):
    if n_clicks > 0:
        if cur_user.is_user_logged_in():
            return ''
        else:
            return 'Incorrect username or password'
    else:
        return ''
