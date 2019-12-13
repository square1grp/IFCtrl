from ..__widget import __Widget
import plotly.graph_objs as go
import dash_core_components as dcc
from querymanager.intelliflux_querymanager import IntelliFluxQueryManager
from server import current_user
from datetime import datetime


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
        sql_query = 'SELECT t_stamp,value, name FROM data WHERE name=\'%s\' AND value > \'%s\' AND t_stamp BETWEEN \'%s 00:00:00\' AND \'%s 00:00:00\';' % (
            self.config['metric'], self.config['flow_min'], time_stamp_from, time_stamp_to)

        flowdata = self.queyManager.getWidgetDataFromQueryManager(
            widget_name, time_stamp_from, time_stamp_to, database_id, sql_query, user_id, True)

        temp_flowdata = dict()
        for idx in flowdata:
            row = flowdata[idx]

            t_stamp = datetime.strptime(
                row['t_stamp'], '%Y-%m-%dT%H:%M:%S.%fZ')

            key = t_stamp.strftime('%Y-%m-%d')

            if key not in temp_flowdata:
                temp_flowdata[key] = []

            temp_flowdata[key].append(
                dict(t_stamp=row['t_stamp'], value=row['value']))

        del flowdata

        self.widget_data = dict()
        for key in temp_flowdata:
            flowdata = temp_flowdata[key]

            prev_time = flowdata[0]['t_stamp']

            if isinstance(prev_time, str):
                prev_time = datetime.strptime(
                    prev_time, '%Y-%m-%dT%H:%M:%S.%fZ')

            flow_total = 0.0

            for row in flowdata[1:]:
                # get the seconds between the previous and the current times
                t_stamp = datetime.strptime(
                    row['t_stamp'], '%Y-%m-%dT%H:%M:%S.%fZ')

                delta = (t_stamp - prev_time).total_seconds()

                # skip rows longer than 2 minutes apart
                if delta > 120:
                    prev_time = t_stamp
                    continue

                # add to the flow totalizer
                flow_total += (row['value'] / 3600.0) * delta

            self.widget_data[key] = flow_total

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
                marker_color=['#10739e', '#f2931e', '#ae4132', '#12aab5', '#23445d'],
                name='data'                 # Name the data series
            )
        ]

    # additional layout
    def get_layout_options(self):
        return dict(xaxis=dict(showticklabels=False), yaxis=dict(showticklabels=False))

    # get graph in the current widget
    def get_widget_graph(self):
        return [
            dcc.Graph(
                figure=go.Figure(
                    data=self.get_graph_data(),
                    layout=self.get_graph_layout(
                        self.get_layout_options())
                ),
                className='m-auto'
            )
        ]
