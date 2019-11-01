import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from classes.content_area import ContentArea
from layouts import header, control, navigation, content
from server import app
from variables import json_data

# create page layout
layout = [
    header.layout,
    control.layout,
    dbc.Row([
        dcc.Location(id='dashboard_url', refresh=False),
        navigation.layout,
        content.layout,
        dbc.Col(className='col-3 d-none d-xl-block')
    ])
]

# show correct page content by the current url
@app.callback(Output('content-area', 'children'),
              [Input('dashboard_url', 'pathname')])
def display_page(pathname):
    slug = ''
    if pathname is not None:
        slug = pathname.replace('/', '')

    slug = slug if slug else json_data['pages'][0]['slug']

    """ Find page object matched with the slug """
    page = [page for page in json_data['pages'] if page['slug'] == slug][0]

    """ If page is not found, show Not Found. """
    if page is None:
        return html.Div(['Not Found'])


    content_area = ContentArea(page)

    return content_area.get_content()
