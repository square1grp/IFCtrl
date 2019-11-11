import dash_bootstrap_components as dbc


def get_layout(nav_items=[]):
    # create nav items
    nav_item_link_list = []
    for nav_item in nav_items:
        nav_item_link_list.append(
            dbc.NavItem(dbc.NavLink(
                nav_item['label'], href=nav_item['target']))
        )

    # create navigation layout
    return dbc.Col(
        [
            dbc.NavbarSimple(
                nav_item_link_list,
                className="px-md-0 px-lg-3"
            )
        ],
        className='col-12 col-md-3 bg-green'
    )
