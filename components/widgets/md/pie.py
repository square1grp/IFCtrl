from ..__widget import __Widget
import plotly.graph_objs as go
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc


class Widget(__Widget):
    def fetch_widget_data(self):
        self.widget_data = [99, 1]

        return self.widget_data

    # get graph data
    def get_graph_data(self, device=None):
        return [go.Pie(
            labels=['', ''],
            values=self.widget_data,
            marker_colors=['#10739E', '#FFFFFF'],
            textinfo='none',
            hoverinfo='none',
            hole=0.5
        )]

    # more layout options
    def get_layout_options(self):
        return dict(
            showlegend=False,
            margin=dict(b=15, t=15, r=15, l=15)
        )

    def get_widget_graph(self):
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
                                '99 %',
                                className='text-center font-weight-bold mt-auto'
                            )
                        ],
                        className='col-md-5 flex-column d-flex m-auto'
                    )
                ],
                className='m-auto d-none d-md-flex'
            )
        ]
