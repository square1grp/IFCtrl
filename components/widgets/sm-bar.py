from .__widget import __Widget
import dash_core_components as dcc
import plotly.graph_objs as go
import random


class Widget(__Widget):

    def get_data(self):
        data_arr = self.config['graph']['data']

        return [
            go.Bar(
                x=data['x'],
                y=data['y'],
                name=data['name'] if data['name'] else data['name'],
                marker=go.bar.Marker(
                    color=data['color'] if data['color'] else 'rgb(%s, %s, %s)' % (
                        random.randint(0, 255),
                        random.randint(0, 255),
                        random.randint(0, 255)
                    )
                )
            ) for data in data_arr
        ]

    def get_content(self):
        return dcc.Graph(
            figure=go.Figure(
                data=self.get_data(),
                layout=self.get_layout()
            ),
            style={
                'height': '200px'
            }
        )
