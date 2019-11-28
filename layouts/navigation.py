import dash_html_components as html
import dash_bootstrap_components as dbc
from classes.User import User

cur_user = User.get_instance()


def get_layout(nav_items=[]):
    # create navigation layout
    return html.Nav(
        children=[
            html.Button(
                '×',
                className='close-nav bg-transparent border-0 col-white'
            ),
            html.A(
                html.Img(
                    src='/assets/images/logo_1.png',
                    height=50,
                ),
                href='/',
                className='d-block text-center my-2'
            ),
            html.Ul(
                children=[
                    html.Li(
                        html.A(
                            children=nav_item['label'],
                            href=nav_item['target']
                        )
                    ) for nav_item in nav_items
                ]
            ),
            html.Form(
                children=[
                    html.Button(
                        children=[
                            dbc.Row(
                                children=[
                                    dbc.Col(
                                        children=[
                                            html.B(
                                                cur_user.get_username()),
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
                        className='bg-black col-white border-0 logout-button px-0'
                    )
                ],
                action='/logout',
                method='post',
            )
        ],
        id='sidebar'
    )
