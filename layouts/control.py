import dash_bootstrap_components as dbc
import dash_html_components as html

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
    className='text-center bg-beige col-black'
)
