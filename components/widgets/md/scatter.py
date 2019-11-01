from ..__widget import __Widget
import plotly.graph_objs as go
import dash_core_components as dcc

class Widget(__Widget):
    
    # get average
    def get_average_data(self, data1, data2):
        return dict(
            x=data1['x'],
            y=[(data1['y'][i] + data2['y'][i])/2 for i in range(len(data1['x']))],
            mode='markers',
            marker=dict(color='#FF8C00', size=8)
        )

    # generate data for bar chart
    def get_graph_data(self, marker_props=[]):
        data_arr = self.config['graph']['data']

        if 'show_average' in self.config['graph'] and\
                self.config['graph']['show_average'] and\
                len(self.config['graph']['data']) == 2:

            avg_data = self.get_average_data(self.config['graph']['data'][0], self.config['graph']['data'][1])
            data_arr.append(avg_data)

        return [
            go.Scatter(
                x=data['x'],
                y=data['y'],
                name=data['name'] if 'name' in data else None,
                fill=data['fill'] if 'fill' in data else None,
                mode=data['mode'] if 'mode' in data else 'lines',
                line=data['line'] if 'line' in data else dict(),
                marker=data['marker'] if 'marker' in data else dict()
            ) for data in data_arr
        ]
    
    # additional layout options
    def get_margin(self):
        return dict(
            margin=dict(b=30, t=40, r=30)
        )

    # get widget graph
    def get_widget_graph(self):
        return [
            dcc.Graph(
                figure=go.Figure(
                    data=self.get_graph_data(),
                    layout=self.get_graph_layout(self.get_margin())
                ),
                className='m-auto'
            )
        ]