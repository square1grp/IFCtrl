from ..__widget import __Widget
import plotly.graph_objs as go
import dash_core_components as dcc
from querymanager.intelliflux_querymanager import IntelliFluxQueryManager
from server import current_user


class Widget(__Widget):
    queyManager = IntelliFluxQueryManager()

    # get widget data via query manager
    def fetch_widget_data(self):
        user_id = current_user.get_user_id()
        time_stamp_from = current_user.get_time_stamp_from()
        time_stamp_to = current_user.get_time_stamp_to()
        database_id = current_user.get_user_database_id()
        widget_name = '%s-widget-%s-%s-%s-user-%s' % (self.widget_type,
                                                      time_stamp_from, time_stamp_to, database_id, user_id)
        sql_query = 'SELECT t_stamp, name, value FROM data WHERE name=\'Permeability\' AND t_stamp BETWEEN \'%s 00:00:00\' AND \'%s 00:00:00\' ORDER BY t_stamp ASC' % (
            time_stamp_from, time_stamp_to)

        self.widget_data = self.queyManager.getWidgetDataFromQueryManager(
            widget_name, time_stamp_from, time_stamp_to, database_id, sql_query, user_id, True)

    # get average
    def get_average_data(self, data1, data2):
        return dict(
            x=data1['x'],
            y=[(data1['y'][i] + data2['y'][i]) /
                2 for i in range(len(data1['x']))],
            mode='markers',
            marker=dict(color='#FF8C00', size=8)
        )

    # generate data for bar chart
    def get_graph_data(self, marker_props=[]):
        return [go.Scatter(
            x=self.widget_data.t_stamp,
            y=self.widget_data.value,
            name=None,
            fill=None,
            mode='lines',
            line=dict(),
            marker=dict()
        )] if self.widget_data else []

    # additional layout options
    def get_layout_options(self):
        return dict(
            margin=dict(b=30, t=40, r=30)
        )

    # get widget graph
    def get_widget_graph(self):
        return [
            dcc.Graph(
                figure=go.Figure(
                    data=self.get_graph_data(),
                    layout=self.get_graph_layout(self.get_layout_options())
                ),
                config=dict(displaylogo=False),
                className='m-auto'
            )
        ]
