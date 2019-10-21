from variables import colors

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go


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
        if 'graph_data' in self.config:
            return dcc.Graph(
                figure={
                    'data': self.config['graph_data'],
                    'layout': {
                        'margin': {'l': 30, 'b': 30, 't': 10, 'r': 10},
                        'showlegend': False,
                        'height': 200 if self.is_child_widget else 410
                    }
                }
            )

        return html.Div(
            style={
                'height': '100%',
                'minHeight': '%spx' % (200 if self.is_child_widget else 410),
                'backgroundColor': self.config['backgroundColor']
            }
        )
