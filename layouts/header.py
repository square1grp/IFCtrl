import dash_core_components as dcc
import dash_bootstrap_components as dbc
from classes.User import User

# get the current user instance
cur_user = User.get_instance()

# create header layout
layout = dbc.Row(
    [
        dbc.Col(
            [
                dcc.LogoutButton(logout_url='/logout',
                                 className='float-right m-3 btn btn-primary')
            ],
            xs=12
        )
    ],
    className='text-center bg-black col-white'
)
