import dash_bootstrap_components as dbc
import dash_html_components as html
from variables import colors

# control area layout
layout = dbc.Row(
    [
        dbc.Col(
            [
                html.H1('Control Area')
            ],
            xs=12
        )
    ],
    style={
        'backgroundColor': colors['beige'],
        'color': colors['black']
    },
    className='text-center'
)
