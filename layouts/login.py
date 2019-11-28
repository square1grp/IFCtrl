import dash_html_components as html
import dash_bootstrap_components as dbc
from server import current_user


# create login layout
def get_layout():
    username = ''
    password = ''

    message = current_user.get_message()

    layout = dbc.Container(
        dbc.Row(
            dbc.Col([
                html.H1('Log In', className='text-center'),
                html.P(
                    message['form'], className='error-message text-center') if message['form'] is not None else None,
                html.Form([
                    dbc.FormGroup([
                        dbc.Label('Username', html_for='username'),
                        dbc.Input(type='text', id='username', name='username',
                                  placeholder='Enter username', value=username, invalid=True if message['form'] or message['username'] else False),
                        dbc.FormFeedback(
                            message['username'],
                            valid=False,
                        ),
                    ]),
                    dbc.FormGroup([
                        dbc.Label('Password', html_for='password'),
                        dbc.Input(type='password', id='password', name='password',
                                  placeholder='Enter password', value=password, invalid=True if message['form'] or message['password'] else False),
                        dbc.FormFeedback(
                            message['password'],
                            valid=False,
                        ),
                    ]),
                    html.Button('Login', type='submit', id='login_button',
                                className='col-12 col-lg-4 float-lg-right btn btn-primary')
                ], action='/login', method='post')
            ], className='col-12 col-md-6 col-lg-4 m-auto'),
            align='center', className='height-100vh'),
        fluid=True)

    return layout
