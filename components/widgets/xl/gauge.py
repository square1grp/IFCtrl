from ..__widget import __Widget
import dash_core_components as dcc
import plotly.graph_objs as go


class Widget(__Widget):
    def get_widget_graph(self):
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=270,
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': "Speed"})
        )
        return [
            dcc.Graph(
                figure=fig
            )
        ]
