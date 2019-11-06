import dash_bootstrap_components as dbc
from variables import json_data

# create nav items
nav_item_link_list = []
for nav_item in json_data['nav']:
    nav_item_link_list.append(
        dbc.NavItem(dbc.NavLink(nav_item['label'], href=nav_item['target']))
    )

# create navigation layout
layout = dbc.Col(
    [
        dbc.NavbarSimple(
            nav_item_link_list,
            className="px-md-0 px-lg-3"
        )
    ],
    className='col-12 col-md-3 bg-green'
)
