import dash_bootstrap_components as dbc


# content layout
# will show widget board feeds or reports on this layout
layout = dbc.Col(
    dbc.Row(
        dbc.Col(
            id="content-area",
            className="p-3"
        )
    ),
    className='col-12 col-md-9 col-xl-6 mx-md-auto bg-blue'
)
