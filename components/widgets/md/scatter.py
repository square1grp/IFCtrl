from ..__widget import __Widget
import plotly.graph_objs as go
import dash_core_components as dcc
from querymanager.intelliflux_querymanager import IntelliFluxQueryManager
import pandas as pd
from classes.User import User


class Widget(__Widget):
    queryManager = IntelliFluxQueryManager()

    def fetch_widget_data(self):
        """
        Get widget data via query manager

        returns: {Dict} A dictionary of the pandas dataframe data from the query manager
        """
        # Create the widget name for the QueryManager
        cur_user = User.get_instance()
        user_id = cur_user.get_user_id()
        time_stamp_from = cur_user.get_time_stamp_from()
        time_stamp_to = cur_user.get_time_stamp_to()
        database_id = cur_user.get_user_database_id()
        widget_name = '%s-widget-%s-%s-%s-%s-user-%s' % (self.widget_type, self.config['title']['text'],
                                                         time_stamp_from, time_stamp_to, database_id, user_id)
        # Define the MySQL query to run
        sql_query = "SELECT t_stamp, value, name FROM data WHERE name=\'" + self.config['metric'] + "\' AND t_stamp BETWEEN \'%s 00:00:00\' AND \'%s 00:00:00\' order by t_stamp" % (
            time_stamp_from, time_stamp_to)

        # Fetch the data from the query manager
        self.widget_data = self.queryManager.getWidgetDataFromQueryManager(
            widget_name, time_stamp_from, time_stamp_to, database_id, sql_query, user_id, True)

        # return the fetched data
        return self.widget_data

    # generate data for bar chart
    def get_graph_data(self, marker_props=[]):
        """
        Generate data for a scatter plot

        Arguments:
            marker_props: {List} Properties for the plot markers

        returns: {List} A lost containing a graph object
        """

        if not self.widget_data:
            return []

        # read the query manager dict into a dataframe
        data = pd.DataFrame.from_dict(self.widget_data, orient="index")

        # return the scatter plot configuration
        return [
            go.Scatter(
                # Use the t_stamp column of the dataframe as X
                x=data['t_stamp'],
                # Use the value column of the dataframe as Y
                y=data['value'],
                # Set plot mode to use markers
                mode=self.config['mode'] if 'mode' in self.config else 'markers',
                name='data'                 # Name the data series
            )
        ]

    # additional layout options
    def get_layout_options(self):
        return dict(
            xaxis=dict(showticklabels=False), yaxis=dict(showticklabels=False),
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
                className='m-auto'
            )
        ]
