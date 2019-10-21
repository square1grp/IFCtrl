import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from variables import colors
from classes.User import User
from server import app

# get the current user instance
cur_user = User.get_instance()

# create header layout
layout = dbc.Row(
    [
        dbc.Col(
            [
                dcc.Location(id='logout_url', refresh=True),
                dbc.Button(
                    'Log out',
                    n_clicks=0,
                    color='primary',
                    id='logout-button',
                    className='float-right m-3'
                )
            ],
            xs=12
        )
    ],
    style={
        'backgroundColor': colors['black'],
        'color': colors['white']
    },
    className='text-center'
)

# log out callback
@app.callback(Output('logout_url', 'pathname'),
              [Input('logout-button', 'n_clicks')])
def user_logout(n_clicks):
    if n_clicks:
        cur_user.user_logout()
        return '/logout'
