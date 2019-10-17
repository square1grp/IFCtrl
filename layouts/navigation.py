import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from variables import colors
from variables import json_data

nav_item_link_list = []
for nav_item in json_data['nav']:
    nav_item_link_list.append(
        dbc.NavItem(dbc.NavLink(nav_item['label'], href=nav_item['target']))
    )

layout = dbc.Col(
    [
        dbc.NavbarSimple(
            nav_item_link_list,
            className="px-md-0 px-lg-3"
        )
    ],
    style={
        'backgroundColor': colors['green']
    },
    className='col-12 col-md-3'
)