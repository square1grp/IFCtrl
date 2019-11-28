import dash
import dash_bootstrap_components as dbc
from classes.User import User

# get the current user instance
current_user = User.get_instance()

external_stylesheets = [
    dbc.themes.BOOTSTRAP,
    # '/assets/css/jquery.dataTables.min.css',
    # '/assets/css/scroller.dataTables.min.css',
]

external_scripts = [
    '/assets/js/jquery-3.3.1.min.js',
    '/assets/js/popper.min.js',
    # '/assets/js/jquery.dataTables.min.js',
    # '/assets/js/dataTables.scroller.min.js',
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
