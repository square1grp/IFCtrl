from ..__widget import __Widget
import dash_core_components as dcc
import plotly.graph_objs as go
import dash_bootstrap_components as dbc
import dash_html_components as html


class Widget(__Widget):
    def get_widget_graph(self):
        data_arr = self.config['graph']['data']

        figs = [go.Figure(
            data=go.Indicator(
                mode="gauge+number",
                value=data['value'],
                domain=dict(x=[0, 1], y=[0, 1]),
                number=dict(suffix=' %'),
                gauge=dict(
                    axis=dict(range=[0, 200], visible=False),
                    bar=dict(color='#00FF00', thickness=1),
                    bordercolor='rgba(0,0,0,0)',
                )
            ),
            layout=self.get_graph_layout(
                dict(margin=dict(l=15, t=15, r=15, b=15), height=100)
            )
        ) for data in data_arr]

        return [dbc.Row([
            dbc.Col(
                [
                    dcc.Graph(figure=fig, className='w-100'),
                    html.P(data_arr[index]['label'], className='text-center')
                ],
                className='col-6 col-lg-3'
            ) for index, fig in enumerate(figs)
        ], className='mx-auto')]
