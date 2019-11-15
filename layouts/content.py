import dash_bootstrap_components as dbc


# content layout
# will show widget board feeds or reports on this layout
def get_layout():
    layout = dbc.Col(
        dbc.Row(
            dbc.Col(
                id="content-area",
                className="p-3"
            )
        ),
        className='col-12 col-xl-9 mx-md-auto'
    )

    return layout
