import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from classes.User import User
from datetime import datetime, timedelta


cur_user = User.get_instance()


# control area layout
def get_layout():
    layout = dbc.Row(children=[
        dbc.Col(
            dbc.Row(children=[
                html.A(
                    html.Img(src='/assets/images/logo_1.png', height=50),
                    href='/',
                    className='col-white d-none d-lg-flex m-2'
                ),
                dbc.Col(
                    dbc.Row(children=[
                        html.Div(
                            children=[
                                html.Label(html.Small('From'),
                                           className='m-0'),
                                dcc.DatePickerSingle(
                                    id='time_stamp_from',
                                    date=(datetime.today() -
                                          timedelta(days=1)).strftime('%Y-%m-%d'),
                                    max_date_allowed=datetime.today(),
                                    display_format='MM / DD'
                                )
                            ],
                            className='d-flex flex-column m-2'
                        ),
                        html.Div(
                            children=[
                                html.Label(html.Small('To'), className='m-0'),
                                dcc.DatePickerSingle(
                                    id='time_stamp_to',
                                    date=datetime.today().strftime('%Y-%m-%d'),
                                    max_date_allowed=datetime.today(),
                                    display_format='MM / DD'
                                )
                            ],
                            className='d-flex flex-column m-2'
                        ),
                        html.Div(
                            children=[
                                html.Label(html.Small('System'),
                                           className='m-0'),
                                dcc.Dropdown(
                                    id='user_database_id',
                                    options=[
                                        dict(
                                            label=database['database_name'],
                                            value=database['user_database_id']
                                        ) for database in cur_user.get_user_databases()
                                    ],
                                    clearable=False,
                                    value=cur_user.get_user_database_id()
                                )
                            ], className='d-flex flex-column m-2'
                        ),
                        html.Div(
                            children=[
                                html.Label(html.Small('Button', className='invisible'),
                                           className='m-0'),
                                dbc.Button(
                                    html.Span('Apply Changes'),
                                    id='submit_filter_button',
                                )
                            ], className='d-flex flex-column m-2'
                        ),
                    ], className='flex-column flex-md-row')
                )
            ]),
            className='px-lg-5'
        ),
        html.Hr(className='w-100 m-0')
    ], className='control-container')

    return layout
