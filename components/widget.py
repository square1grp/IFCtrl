from variables import colors

import dash_bootstrap_components as dbc
import dash_html_components as html


# widget class
class Widget:
    is_child_widget = False
    config = {
        'backgroundColor': colors['purple']
    }

    def __init__(self, config, is_child_widget=False):
        self.config = config
        self.is_child_widget = is_child_widget

    # content which draws a widget
    def get_content(self):
        return html.Div(
            style={
                'height': '100%',
                'minHeight': '%spx' % (125 if self.is_child_widget else 260),
                'backgroundColor': self.config['backgroundColor']
            }
        )
