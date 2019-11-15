import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
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
            html.Nav([
                html.Div(id='dismiss'),
                html.Ul([html.Li(html.A(nav_item['label'], href=nav_item['target']))
                         for nav_item in nav_items], className='list-unstyled components')
            ], id='sidebar', className='mCustomScrollbar'),
            dbc.Container([
                header.get_layout()
            ], fluid=True, className='content')
        ], className='wrapper'),
        html.Div(className='overlay'),
        dji.Import(src='/assets/js/scripts.js')
    ]


'''
    # create page layout
    layout = [
        header.layout,
        control.layout,
        dbc.Row([
            dcc.Location(id='dashboard_url', refresh=False),
            navigation.get_layout(nav_items),
            content.layout,
            dbc.Col(className='col-3 d-none d-xl-block')
        ])
    ]

    return dbc.Container(layout, fluid=True)

# show correct page content by the current url
@app.callback(Output('content-area', 'children'),
              [Input('dashboard_url', 'pathname')])
def display_page(pathname):
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
'''
