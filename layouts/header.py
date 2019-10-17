import dash_html_components as html
import dash_bootstrap_components as dbc
from variables import colors


layout = dbc.Row(
    [
        dbc.Col(
            [
                html.H1('Header / Title Area')
            ],
            xs=12
        )
    ],
    style={
        'backgroundColor': colors['black'],
        'color': colors['white']
    },
    className='text-center'
)
