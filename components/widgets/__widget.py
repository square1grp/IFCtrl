from variables import colors
import dash_html_components as html
import plotly.graph_objs as go


# widget abstract class
class __Widget:
    is_child_widget = False
    config = {
        'backgroundColor': colors['purple']
    }

    def __init__(self, config, is_child_widget=False):
        self.config = config
        self.is_child_widget = is_child_widget

    def get_data(self):
        return self.config['graph']['data']

    def get_layout(self):
        layout = self.config['graph']['layout']

        return go.Layout(
            title=go.layout.Title(
                text=layout['title']['text'] if layout['title']['text'] else '',
                x=layout['title']['pos_x'] if layout['title']['pos_x'] else 0.5,
                y=layout['title']['pos_y'] if layout['title']['pos_y'] else 0.9
            ),
            showlegend=True if layout['showLegend'] else False,
            legend=go.layout.Legend(
                x=layout['legend']['pos_x'] if layout['legend']['pos_x'] else 0,
                y=layout['legend']['pos_y'] if layout['legend']['pos_y'] else 1.0,
            ),
            margin=go.layout.Margin(
                l=layout['margin']['left'] if layout['margin']['left'] else 30,
                r=layout['margin']['right'] if layout['margin']['right'] else 10,
                t=layout['margin']['top'] if layout['margin']['top'] else 10,
                b=layout['margin']['bottom'] if layout['margin']['bottom'] else 30
            )
        )

    # content which draws a widget
    def get_content(self):
        return html.Div(
            style={
                'height': '100%',
                'minHeight': '%spx' % (200 if self.is_child_widget else 410),
                'backgroundColor': self.config['backgroundColor']
            }
        )
