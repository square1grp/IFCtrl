import dash_bootstrap_components as dbc
import dash_html_components as html

from variables import colors

# content layout
# will show widget board feeds or reports on this layout
layout = dbc.Col(
    dbc.Row(
        dbc.Col(
            id="content-area",
            className="p-3"
        )
    ),
    style={'backgroundColor': colors['blue']},
    className='col-12 col-md-6 mx-md-auto'
)
