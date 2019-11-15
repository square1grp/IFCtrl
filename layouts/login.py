import dash_html_components as html
import dash_bootstrap_components as dbc
import config

username = config.username if config.username else ''
password = config.password if config.password else ''

# create login layout


def get_layout():
    layout = dbc.Container(
        dbc.Row(
            dbc.Col([
                html.H1('Log In', className='text-center'),
                html.Form([
                    dbc.FormGroup([
                        dbc.Label('Username', html_for='username'),
                        dbc.Input(type='text', id='username', name='username',
                                  placeholder='Enter username', value=username)
                    ]),
                    dbc.FormGroup([
                        dbc.Label('Password', html_for='password'),
                        dbc.Input(type='password', id='password', name='password',
                                  placeholder='Enter password', value=password)
                    ]),
                    html.Button('Login', type='submit',
                                className='col-12 col-lg-4 float-lg-right btn btn-primary')
                ], action='/login', method='post')
            ], className='col-12 col-md-6 col-lg-4 m-auto'),
            align='center', className="height-100vh"),
        fluid=True)

    return layout
