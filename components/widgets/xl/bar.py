from ..__widget import __Widget
import plotly.graph_objs as go
import dash_core_components as dcc


class Widget(__Widget):
    # generate data for bar chart
    def get_graph_data(self, marker_props=[]):
        data_arr = self.config['graph']['data']

        return [
            go.Bar(
                x=data['x'],
                y=data['y'],
                name=data['name'] if 'name' in data else None,
                marker=self.get_data_marker(data, marker_props, 'y')
            ) for data in data_arr
        ]
    
    # get mobile layout
    def get_layout_mobile_options(self):
        return dict(
            margin=dict(b=20, t=40, r=20)
        )
    
    # get graph in the current widget
    def get_widget_graph(self):
        return [
            dcc.Graph(
                figure=go.Figure(
                    data=self.get_graph_data(marker_props=['colorscale', 'line_color', 'line_width', 'showscale', 'colorbar']),
                    layout=self.get_graph_layout()
                ),
                className='m-auto d-none d-xl-block'
            ),
            dcc.Graph(
                figure=go.Figure(
                    data=self.get_graph_data(marker_props=['colorscale', 'line_color', 'line_width']),
                    layout=self.get_graph_layout(self.get_layout_mobile_options())
                ),
                className='m-auto d-xl-none'
            )
        ]