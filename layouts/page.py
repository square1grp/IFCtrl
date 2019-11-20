import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from classes.content_area import ContentArea
from layouts import header, control, navigation, content
from server import app
from classes.User import User
import dash_defer_js_import as dji


# get the current user instance
cur_user = User.get_instance()


def get_layout():
    nav_items = cur_user.get_page_nav_items()

    return [
        html.Div([
            # create navigation layout
            navigation.get_layout(nav_items),
            dbc.Container(
                children=[
                    header.get_layout(),
                    control.get_layout(),
                    dbc.Row(children=[
                        dcc.Location(id='dashboard_url', refresh=False),
                        content.get_layout(),
                        dbc.Col(className='col-3 d-none d-xl-block')
                    ])
                ],
                fluid=True,
                className='content'
            )
        ], className='wrapper'),
        html.Div(id='overlay'),
        dji.Import(src='/assets/js/scripts.js')
    ]


# show correct page content by the current url
@app.callback(Output('content-area', 'children'),
              [Input('dashboard_url', 'pathname'),
               Input('submit_filter_button', 'n_clicks')],
              [State('time_stamp_from', 'date'),
               State('time_stamp_to', 'date'),
               State('user_database_id', 'value')])
def display_page(pathname, n_clicks, time_stamp_from, time_stamp_to, database_id):
    if n_clicks and n_clicks > 0:
        cur_user.set_time_stamp_from(time_stamp_from)
        cur_user.set_time_stamp_to(time_stamp_to)
        cur_user.set_user_database_id(database_id)

    slug = ''
    if pathname is not None:
        slug = pathname.replace('/', '')

    page_items = cur_user.get_page_items()
    if not len(page_items):
        return html.Div()

    slug = slug if slug else page_items[0]['slug']

    """ Find page object matched with the slug """
    page = [page for page in page_items if page['slug'] == slug][0]

    """ If page is not found, show Not Found. """
    if page is None:
        return html.Div(['Not Found'])

    content_area = ContentArea(page)

    return content_area.get_content()
