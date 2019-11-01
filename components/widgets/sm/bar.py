from ..__widget import __Widget
import plotly.graph_objs as go
import dash_core_components as dcc


class Widget(__Widget):    
    # get data marker
    def get_data_marker(self, data, marker_props):
        go_marker = dict()

        if 'marker' not in data:
            return go_marker
        
        for prop in marker_props:
            if prop in data['marker']:
                go_marker[prop] = data['marker'][prop]
        
                if prop == 'colorscale':
                    go_marker['color'] = data['y']
        
        return go_marker

    # generate data for bar chart
    def get_graph_data(self, marker_props=[]):
        data_arr = self.config['graph']['data']

        return [
            go.Bar(
                x=data['x'],
                y=data['y'],
                name=data['name'] if 'name' in data else None,
                marker=self.get_data_marker(data, marker_props)
            ) for data in data_arr
        ]
    
    # get mobile layout
    def get_mobile_layout(self):
        return dict(
            margin=dict(b=20, t=40, r=20)
        )
    
    # get graph in the current widget
    def get_widget_graph(self):
        mobile_layout = self.get_mobile_layout()

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
                    layout=self.get_graph_layout(mobile_layout)
                ),
                className='m-auto d-xl-none'
            )
        ]