import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from classes.User import User
from datetime import datetime


cur_user = User.get_instance()


# control area layout
def get_layout():
    user_databases = cur_user.get_user_databases()

    layout = dbc.Row(children=[
        dbc.Col(
            dbc.Row(children=[
                html.A(
                    html.Img(src='/assets/images/logo_1.png', height=50),
                    href='/', className='col-white d-flex m-2'
                ),
                dbc.Col(
                    dbc.Row(children=[
                        html.Div(
                            children=[
                                html.Label(html.Small('From'),
                                           className='m-0'),
                                dcc.DatePickerSingle(
                                    date=datetime.now(),
                                    max_date_allowed=datetime.now(),
                                    display_format='MM / DD'
                                )
                            ],
                            className='d-flex flex-column mr-2'
                        ),
                        html.Div(
                            children=[
                                html.Label(html.Small('To'), className='m-0'),
                                dcc.DatePickerSingle(
                                    date=datetime.now(),
                                    max_date_allowed=datetime.now(),
                                    display_format='MM / DD'
                                )
                            ],
                            className='d-flex flex-column mr-2'
                        ),
                        html.Div(
                            children=[
                                html.Label(html.Small('System'),
                                           className='m-0'),
                                dcc.Dropdown(
                                    options=[
                                        dict(
                                            label=database['database_name'],
                                            value=database['user_database_id']
                                        ) for database in user_databases
                                    ],
                                    clearable=False,
                                    value=list(user_databases)[0]['user_database_id'] if len(user_databases) else None)
                            ], className='d-flex flex-column'),
                    ])
                )
            ]),
            className='px-5'
        ),
        html.Hr(className='w-100 m-0')
    ], className='control-container')

    return layout
