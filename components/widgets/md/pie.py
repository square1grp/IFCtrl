from ..__widget import __Widget
import plotly.graph_objs as go
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc


class Widget(__Widget):
    # get graph data
    def get_graph_data(self, device=None):
        data_arr = self.config['graph']['data']

        if not len(data_arr):
            return []

        return [go.Pie(
            labels=data_arr[0]['labels'],
            values=data_arr[0]['values'],
            marker=self.get_data_marker(data_arr[0], ['colors']),
            textinfo='none',
            hole=0.5 if device == 'mobile' else None
        )]

    # more layout options
    def get_layout_options(self):
        return dict(
            margin=dict(b=15, t=15, r=15, l=15)
        )

    # add total to the center of the chart
    def get_layout_mobile_options(self, total_text):
        return dict(
            margin=dict(b=15, t=15, r=15, l=15),
            annotations=[
                dict(
                    text=total_text,
                    x=0.5,
                    y=0.6,
                    font_size=30,
                    font_color='#000000',
                    showarrow=False
                ),
                dict(
                    text='Total Cleans',
                    x=0.5,
                    y=0.4,
                    font_size=15,
                    font_color='#000000',
                    showarrow=False
                )
            ]
        )

    # get_widget_graph
    def get_widget_graph(self):
        total_text = sum(self.config['graph']['data'][0]['values'])

        return [
            dbc.Row(
                [
                    dbc.Col(
                        dcc.Graph(
                            figure=go.Figure(
                                data=self.get_graph_data(),
                                layout=self.get_graph_layout(
                                    self.get_layout_options())
                            ),
                            className='m-auto'
                        ),
                        className='col-md-7'
                    ),
                    dbc.Col(
                        [
                            html.H1(
                                total_text,
                                className='text-center font-weight-bold mt-auto'
                            ),
                            html.H5(
                                'Total Cleans',
                                className='text-center font-weight-bold mb-auto'
                            ),
                        ],
                        className='col-md-5 flex-column d-flex m-auto'
                    )
                ],
                className='m-auto d-none d-md-flex'
            ),
            dcc.Graph(
                figure=go.Figure(
                    data=self.get_graph_data('mobile'),
                    layout=self.get_graph_layout(
                        self.get_layout_mobile_options(total_text))
                ),
                className='m-auto d-md-none'
            )
        ]
