import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from server import app
from classes.User import User

username = ''
password = ''

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


@app.callback(Output('login_url', 'pathname'),
              [Input('login-button', 'n_clicks')],
              [State('username', 'value'),
               State('password', 'value')])
def user_login(n_clicks, username, password):
    if cur_user.user_login(username, password):
        return '/'
