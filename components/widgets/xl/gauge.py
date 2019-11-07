from ..__widget import __Widget
import dash_core_components as dcc
import plotly.graph_objs as go


class Widget(__Widget):
    def get_widget_graph(self):
        data_arr = self.config['graph']['data']

        figs = [go.Figure(go.Indicator(
            mode="gauge+number",
            value=data['value'],
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': "Speed"})
        ) for data in data_arr]

        return [
            dcc.Graph(figure=fig, className='col-12 col-md-6 col-xl-3') for fig in figs
        ]
