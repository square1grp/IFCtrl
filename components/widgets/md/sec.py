from ..__widget import __Widget
import plotly.graph_objs as go
import dash_core_components as dcc
import dash_bootstrap_components as dbc


class Widget(__Widget):
    def fetch_widget_data(self):
        pass

    def get_widget_graph(self):
        return [
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(
                        figure=go.Figure(
                            data=go.Bar(x=['0', '1', '2', '3', '4'],
                                        y=[30, 40, 50, 20, 10],
                                        marker_color=['#10739e', '#f2931e', '#ae4132', '#12aab5', '#23445d']),
                            layout=self.get_graph_layout(
                                dict(xaxis=dict(showticklabels=False),
                                     yaxis=dict(showticklabels=False)))
                        ),
                    ), className='col-8'),
                    dbc.Col(
                        dbc.Row(
                            [
                                dbc.Col(dcc.Graph(
                                    figure=go.Figure(
                                        data=go.Indicator(
                                            mode="gauge",
                                            value=200,
                                            gauge=dict(
                                                axis=dict(
                                                    range=[0, 200], visible=False),
                                                bar=dict(color='#10739E',
                                                         thickness=1),
                                                bordercolor='rgba(0,0,0,0)',
                                            )
                                        ),
                                        layout=self.get_graph_layout(
                                            dict(margin=dict(l=15, t=15,
                                                             r=15, b=15), height=100)
                                        )
                                    )
                                ), className='m-auto'),
                                dbc.Col(dcc.Graph(
                                    figure=go.Figure(
                                        data=go.Indicator(
                                            mode="gauge",
                                            value=200,
                                            gauge=dict(
                                                axis=dict(
                                                    range=[0, 200], visible=False),
                                                bar=dict(color='#10739E',
                                                         thickness=1),
                                                bordercolor='rgba(0,0,0,0)',
                                            )
                                        ),
                                        layout=self.get_graph_layout(
                                            dict(margin=dict(l=15, t=15,
                                                             r=15, b=15), height=100)
                                        )
                                    )
                                ), className='m-auto')
                            ],
                            className='flex-column h-100'
                        ), className='col-4')
                ],
                className='mx-auto'
            )
        ]
