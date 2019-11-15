import dash_html_components as html
import dash_bootstrap_components as dbc


def get_layout(nav_items=[]):
    # create navigation layout
    return html.Nav([
        # html.Div(id='dismiss'),
        html.Ul([html.Li(html.A(nav_item['label'], href=nav_item['target']))
                 for nav_item in nav_items], className='list-unstyled components')
    ], id='sidebar', className='mCustomScrollbar _mCS_1 mCS-autoHide mCS_no_scrollbar')
