"""
IntelliFlux Dashboard Query Mananger
-------------
This Query Manager class implement the caching mechanism and serve the data for Intelliflux Dashboard by optimizing the performance
using Panda Data Frames and Pickels for caching purpose

"""
import json
import pandas as pd
from .intelliflux_dashboard_api_consumer import *
import pandasql as psql
from .sql_query_parser import *


class IntelliFluxQueryManager(object):

    """
    This method provides the data for widgets and manage the cache

    """

    def getWidgetDataFromQueryManager(self, widget_name, time_stamp_from, time_stamp_to, database_id, sql_query, user_id, is_json_reponse):
        try:
            widget_name = str(user_id)+'_'+widget_name.replace(" ", "_")
            widget_data = None
            master_data_frame = self.loadMasterDataFrame()
            if master_data_frame is None:
                master_data_frame = self.createMasterDataframe()
                if master_data_frame is not None:
                    json_widget_data = getWidgetData(database_id, sql_query)
                    widget_data = pd.read_json(json_widget_data)
                    widget_data.to_pickle(widget_name+'.pkl')
                    self.addNewRefrenceInMasterDataframe(
                        master_data_frame, widget_name, time_stamp_from, time_stamp_to)
            else:
                reference_df = self.getWidgetDataFrameRefrence(
                    master_data_frame, widget_name)
                if reference_df.count().key == 1:
                    widget_data_frame = df = pd.read_pickle(widget_name+'.pkl')
                    panda_Sql_query = self.getPandaSqlQuery(
                        sql_query, 'widget_data_frame')
                    if time_stamp_from is not None and time_stamp_to is not None:
                        if time_stamp_from >= reference_df.time_stamp_from.item() and time_stamp_to <= reference_df.time_stamp_to.item():
                            widget_data = psql.sqldf(panda_Sql_query, locals())
                            print(widget_data)
                        elif time_stamp_from > reference_df.time_stamp_to.item():
                            modified_query = replace_date_filters(
                                sql_query, reference_df.time_stamp_to.item())
                            json_widget_data = getWidgetData(
                                database_id, modified_query)
                            widget_data_from_db = pd.read_json(
                                json_widget_data)
                            widget_data_frame = widget_data_frame.append(
                                widget_data_from_db, ignore_index=True)
                            widget_data = psql.sqldf(panda_Sql_query, locals())
                            self.updateMasterDataFrame(
                                master_data_frame, widget_name, reference_df.time_stamp_from.item(), time_stamp_to)
                        else:
                            print("No matched")
                    else:
                        widget_data = psql.sqldf(panda_Sql_query, locals())
                else:
                    json_widget_data = getWidgetData(database_id, sql_query)
                    widget_data = pd.read_json(json_widget_data)
                    self.addNewRefrenceInMasterDataframe(
                        master_data_frame, widget_name, time_stamp_from, time_stamp_to)
        except (Exception) as error:
            print(error)
        finally:
            print('Process completed.')

        return widget_data

    # Load Master Dataframe from Memory
    def loadMasterDataFrame(self):
        try:
            df = pd.read_pickle("master.pkl")
            print(df)
            return df
        except (Exception) as error:
            print(error)
            return None

    # Create Master Dataframe
    def createMasterDataframe(self):
        try:
            master_data_frame = pd.DataFrame(
                columns=['key', 'time_stamp_from', 'time_stamp_to'])
            master_data_frame.to_pickle('master.pkl')
            return master_data_frame
        except (Exception) as error:
            print(error)
        return None

    # Add refrence of new widget cache in Master Dataframe
    def addNewRefrenceInMasterDataframe(self, master_data_frame, widget_name, time_stamp_from, time_stamp_to):
        status = False
        try:
            updated_df = master_data_frame.append(pd.DataFrame({'key': [widget_name], 'time_stamp_from': [
                                                  time_stamp_from], 'time_stamp_to': time_stamp_to}), ignore_index=True)
            updated_df.to_pickle('master.pkl')
            status = True
        except (Exception) as error:
            print(error)
        return status

    # Update Master Dataframe incase of change in date filters
    def updateMasterDataFrame(self, dataFrameToUpdate, key, time_stamp_from, time_stamp_to):
        status = False
        try:
            dataFrameToUpdate.loc[dataFrameToUpdate.key ==
                                  key, 'time_stamp_from'] = time_stamp_from
            dataFrameToUpdate.loc[dataFrameToUpdate.key ==
                                  key, 'time_stamp_to'] = time_stamp_to
            dataFrameToUpdate.to_pickle('master.pkl')
            status = True
        except (Exception) as error:
            print(error)
        return status

    # Get detail of widget cache file from Master Data Frame
    def getWidgetDataFrameRefrence(self, master_data_frame, widget_name):
        widget_data = master_data_frame.loc[master_data_frame['key']
                                            == widget_name]
        return widget_data

    def jsonloads(self, text):
        index, values = json.loads(text)
        return pd.read_json

    # Create panda SQL query
    def getPandaSqlQuery(self, sql_query, widget_name):
        sql_table_name = extract_tables(sql_query)
        panda_sql_query = sql_query.replace(sql_table_name, widget_name)
        return panda_sql_query
