import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from server import app
from classes.User import User

from views import login

cur_user = User.get_instance()

app.layout = html.Div(
    [
        dbc.Container(id='page-content', fluid=True),
        dcc.Location(id='page_url', refresh=False),
    ]
)


@app.callback(Output('page-content', 'children'),
              [Input('page_url', 'pathname')])
def display_page(pathname):
    print(cur_user.is_user_logged_in())
    if pathname == '/login' and not cur_user.is_user_logged_in():
        return login.layout

    if not cur_user.is_user_logged_in():
        return dcc.Location(pathname='/login', id='redirect_to_login')


if __name__ == '__main__':
    app.run_server(debug=True)
