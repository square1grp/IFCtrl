import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from server import app
from classes.User import User
from layouts import login, page
import config

# get the current user instance
cur_user = User.get_instance()

# create page layout
app.layout = html.Div(
    [
        # container for the page content
        dbc.Container(id='page-content', fluid=True),
        # url management
        dcc.Location(id='page_url', refresh=False),
    ]
)

# callbacks, show page content under correct page urls
@app.callback(Output('page-content', 'children'),
              [Input('page_url', 'pathname')])
def display_page(pathname):
    # check if the current page is login page or user is not logged in
    # if yes, show login page
    if pathname == '/login' and not cur_user.is_user_logged_in():
        return login.layout

    # if page is not login page and user is not logged in,
    # redriect to login page
    if not cur_user.is_user_logged_in():
        return dcc.Location(pathname='/login', id='redirect_to_login')

    # show pages
    return page.layout


# run the server
if __name__ == '__main__':
    # debug mode True/False
    # host ip ex: 127.0.0.1 (local), 0.0.0.0 (public)
    app.run_server(debug=config.dev_env, host=config.host_ip)
