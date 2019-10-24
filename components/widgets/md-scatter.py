from .__widget import __Widget
import dash_core_components as dcc
import plotly.graph_objs as go
import random


class Widget(__Widget):

    def get_data(self):
        data_arr = self.config['graph']['data']

        return [
            go.Scatter(
                x=data['x'],
                y=data['y'],
                mode=data['mode'],
                name=data['name'] if data['name'] else '',
                marker=go.scatter.Marker(
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
            className='m-auto'
        )
