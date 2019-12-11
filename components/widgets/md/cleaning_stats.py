from ..__widget import __Widget
import plotly.graph_objs as go
import dash_core_components as dcc
from querymanager.intelliflux_querymanager import IntelliFluxQueryManager
from server import current_user


class Widget(__Widget):
    queyManager = IntelliFluxQueryManager()

    # get widget data via query manager
    def fetch_widget_data(self):
        self.widget_data = []
        user_id = current_user.get_user_id()
        time_stamp_from = current_user.get_time_stamp_from()
        time_stamp_to = current_user.get_time_stamp_to()
        database_id = current_user.get_user_database_id()
        widget_name = '%s-widget-%s-%s-%s-user-%s' % (self.widget_type,
                                                      time_stamp_from, time_stamp_to, database_id, user_id)

        for mode in self.config['mode'].split('+'):
            if mode == 'total':
                sql_query = 'SELECT COUNT(DISTINCT(startTime)) as count FROM cleans WHERE startTime BETWEEN \'%s 00:00:00\' AND \'%s 00:00:00\'' % (
                    time_stamp_from, time_stamp_to)
            elif mode == 'common':
                sql_query = 'SELECT intensity, count(DISTINCT(startTime)) as count FROM cleans WHERE startTime BETWEEN \'%s 00:00:00\' AND \'%s 00:00:00\' GROUP BY intensity ORDER BY count DESC LIMIT 1' % (
                    time_stamp_from, time_stamp_to)
            elif mode == 'time':
                sql_query = 'SELECT (SUM(TIMESTAMPDIFF(SECOND, startTime, endTime)) / 60 / 60) as time FROM cleans WHERE startTime BETWEEN \'%s 00:00:00\' AND \'%s 00:00:00\'' % (
                    time_stamp_from, time_stamp_to)
            elif mode == 'use':
                sql_query = 'SELECT SUM(JSON_EXTRACT(profile, \'$.WaterUsage\')) as usage FROM cleans WHERE startTime BETWEEN \'%s 00:00:00\' AND \'%s 00:00:00\'' % (
                    time_stamp_from, time_stamp_to)

            self.widget_data.append(dict(
                mode=mode,
                value=self.queyManager.getWidgetDataFromQueryManager(
                    widget_name, time_stamp_from, time_stamp_to, database_id, sql_query, user_id, True)
            ))

        # return the fetched data
        return self.widget_data
