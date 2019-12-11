from ..__widget import __Widget
import plotly.graph_objs as go
import dash_core_components as dcc
from querymanager.intelliflux_querymanager import IntelliFluxQueryManager
from server import current_user
from datetime import datetime
from statistics import mean


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

        # t_stamp = 'DATE_FORMAT(t_stamp, \'%Y-%m-%d\')'
        # sql_query = 'SELECT name, AVG(value) as value, %s as t_stamp FROM data WHERE name=\'%s\' AND value > %s AND t_stamp BETWEEN \'%s\' AND \'%s\' group by %s;' % (
        #     t_stamp, self.config['metric'], self.config['flow_min'], time_stamp_from, time_stamp_to, t_stamp)
        sql_query = 'SELECT 0 as i, COUNT(id) as count FROM %s WHERE relativeIntensity=0 AND startTime BETWEEN \'%s 00:00:00\' AND \'%s 00:00:00\'' % (
            self.config['metric'], time_stamp_from, time_stamp_to)

        cleaning_levels_data = self.queyManager.getWidgetDataFromQueryManager(
            widget_name, time_stamp_from, time_stamp_to, database_id, sql_query, user_id, True)

        self.widget_data = cleaning_levels_data

        # return the fetched data
        return self.widget_data

    # generate data for bar chart
    def get_graph_data(self):
        if not self.widget_data:
            return []

        # read the query manager dict into a dataframe
        # data = pd.DataFrame.from_dict(self.widget_data, orient="index")

        return [
            go.Bar(
                x=list(self.widget_data.keys()),
                y=list(self.widget_data.values()),
                name='data'                 # Name the data series
            )
        ]

    # get graph in the current widget
    def get_widget_graph(self):
        return [
            dcc.Graph(
                figure=go.Figure(
                    data=self.get_graph_data(),
                    layout=self.get_graph_layout()
                ),
                className='m-auto'
            )
        ]
