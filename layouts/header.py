import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from classes.User import User

# get the current user instance
cur_user = User.get_instance()


# create header layout
def get_layout():
    layout = dbc.Row(
        dbc.Col(
            dbc.Row(children=[
                dbc.Button(
                    html.Span(
                        html.I(
                            className='fa fa-bars',
                            **{'aria-hidden': True}
                        )
                    ),
                    id='sidebarCollapse',
                    className='m-2 bg-transparent px-3'
                ),
                html.A(
                    children=[
                        html.Img(
                            src='/assets/images/logo.png',
                            height=50, width=50
                        ),
                        html.Div(
                            html.Big(
                                children=[
                                    'IntelliFlux ',
                                    html.B('Dashboard')
                                ],
                                className='m-auto'
                            ),
                            className='ml-2 d-flex flex-column '
                        )
                    ], href='/', className='col-white d-flex m-2'),
                html.Form(
                    children=[
                        html.Button(
                            children=[
                                dbc.Row(
                                    children=[
                                        dbc.Col(
                                            children=[
                                                html.B(
                                                    cur_user.get_user_name()),
                                                html.Span('Logout')
                                            ],
                                            className='d-flex flex-column p-0'
                                        ),
                                        dbc.Col(
                                            children=[
                                                html.Span(
                                                    html.I(
                                                        className='fa fa-user-circle',
                                                        **{'aria-hidden': True}
                                                    ),
                                                    className='m-auto'
                                                )
                                            ],
                                            className='d-flex flex-column pr-0'
                                        )
                                    ],
                                    className='m-auto'
                                )
                            ],
                            type='submit',
                            className='bg-black col-white border-0 logout-button'
                        )
                    ],
                    action='/logout',
                    method='post',
                    className='ml-auto m-2'
                )
            ]),
            className='bg-black px-5'
        ),
        className='header-container'
    )

    return layout
