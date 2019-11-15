import dash
import dash_bootstrap_components as dbc

external_stylesheets = [
    dbc.themes.BOOTSTRAP,
    '/assets/css/jquery.mCustomScrollbar.min.css',
]

external_scripts = [
    '/assets/js/jquery-3.3.1.slim.min.js',
    '/assets/js/popper.min.js',
]

# Create dash app
app = dash.Dash(
    __name__,
    external_stylesheets=external_stylesheets,
    external_scripts=external_scripts,
    suppress_callback_exceptions=True,
    meta_tags=[{
        'name': 'viewport',
        'content': 'width=device-width, initial-scale=1.0'
    }]
)
