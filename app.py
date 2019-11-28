import flask
import dash_html_components as html
from dash.dependencies import Input, Output
from server import app
from classes.User import User
from layouts import page, login
import config

# Create a login route
@app.server.route('/login', methods=['POST'])
def route_login():
    # get the current user instance
    cur_user = User.get_instance()

    data = flask.request.form
    username = data.get('username')
    password = data.get('password')

    cur_user.set_auth(username=username, password=password)

    if not username or not password:
        cur_user.set_message(dict(
            form=None,
            username='Username is required' if not username else '',
            password='Password is required' if not password else '',
        ))

        return flask.redirect('/login')

    # actual implementation should verify the password.
    # Recommended to only keep a hash in database and use something like
    # bcrypt to encrypt the password and check the hashed results.

    # Return a redirect with
    if cur_user.user_login(username, password):
        rep = flask.redirect('/')

        # Here we just store the given username in a cookie.
        # Actual session cookies should be signed or use a JWT token.
        token = cur_user.get_token()

        rep.set_cookie('if-web-dashboard-token', token)
        return rep

    cur_user.set_message(dict(
        form='Username or Password is incorrect.',
        username=None,
        password=None
    ))
    return flask.redirect('/login')

# create a logout route
@app.server.route('/logout', methods=['POST'])
def route_logout():
    # get the current user instance
    cur_user = User.get_instance()
    cur_user.set_auth(username='', password='')

    # Redirect back to the index and remove the session cookie.
    rep = flask.redirect('/')
    rep.set_cookie('if-web-dashboard-token', '', expires=0)
    return rep


# create page layout
app.layout = html.Div(id='if-web-auth-frame')

@app.callback(Output('if-web-auth-frame', 'children'),
              [Input('if-web-auth-frame', 'id')])
def dynamic_layout(_):
    # get the current user instance
    cur_user = User.get_instance()

    token = flask.request.cookies.get('if-web-dashboard-token')

    if not token:
        # If there's no cookie we need to login.
        return login.get_layout()

    cur_user.set_token(token)

    if cur_user.get_user_data() is None:
        # If there's no cookie we need to login.
        return login.get_layout()

    return page.get_layout()


# run the server
if __name__ == '__main__':
    # debug mode True/False
    # host ip ex: 127.0.0.1 (local), 0.0.0.0 (public)
    app.run_server(debug=config.dev_env, host=config.host_ip)
