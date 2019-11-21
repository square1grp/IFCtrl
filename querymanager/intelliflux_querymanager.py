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
from sqlparse.sql import IdentifierList, Identifier
from sqlparse.tokens import Keyword, DML
from datetime import datetime, timedelta


class IntelliFluxQueryManager(object):

    """
    This method provides the data for widgets and manage the cache

    """

    def getWidgetDataFromQueryManager(self, widget_name, time_stamp_from, time_stamp_to, database_id, sql_query, user_id, is_json_reponse):
        try:
            cache_expiry_date = datetime.now() + timedelta(days=-30)
            widget_name = str(user_id)+'_'+str(database_id) + \
                '_'+widget_name.replace(" ", "_")
            widget_data = None
            master_data_frame = self.loadMasterDataFrame()
            # print(master_data_frame)
            # return master_data_frame
            if master_data_frame is None:
                master_data_frame = self.createMasterDataframe()
                if master_data_frame is not None:
                    json_widget_data = getWidgetData(database_id, sql_query)
                    widget_data = pd.read_json(json_widget_data)
                    # If executed query have date filters then add it to cache for serving same data in future from cache
                    if time_stamp_from is not None and time_stamp_to is not None:
                        widget_data.to_pickle(
                            'panda_cache/'+widget_name+'.pkl')
                        self.addNewRefrenceInMasterDataframe(
                            master_data_frame, widget_name, user_id, database_id, time_stamp_from, time_stamp_to)
            else:
                cache_data_detail_df = self.getWidgetDataFrameRefrence(
                    master_data_frame, widget_name, user_id, database_id)
                if cache_data_detail_df.count().widget_name == 1:
                    cached_widget_data = self.loadCachedDataFrames(widget_name)
                    panda_Sql_query = self.getPandaSqlQuery(
                        sql_query, 'cached_widget_data')
                    if time_stamp_from is not None and time_stamp_to is not None and cache_data_detail_df.last_modification_time.item() > cache_expiry_date:
                        if time_stamp_from >= cache_data_detail_df.time_stamp_from.item() and time_stamp_to <= cache_data_detail_df.time_stamp_to.item():
                            widget_data = psql.sqldf(panda_Sql_query, locals())
                            print(widget_data)
                        elif time_stamp_from > cache_data_detail_df.time_stamp_to.item() or time_stamp_to > cache_data_detail_df.time_stamp_to.item():
                            modified_query = replace_date_filters(
                                sql_query, time_stamp_from, cache_data_detail_df.time_stamp_to.item())
                            json_widget_data = getWidgetData(
                                database_id, modified_query)
                            widget_data_from_db = pd.read_json(
                                json_widget_data)
                            cached_widget_data = cached_widget_data.append(
                                widget_data_from_db, ignore_index=True)
                            widget_data = psql.sqldf(panda_Sql_query, locals())
                            self.updateMasterDataFrame(
                                master_data_frame, widget_name, user_id, database_id, cache_data_detail_df.time_stamp_from.item(), time_stamp_to)
                        else:
                            print("No matched")
                    else:
                        json_widget_data = getWidgetData(
                            database_id, sql_query)
                        widget_data = pd.read_json(json_widget_data)
                        widget_data.to_pickle(
                            'panda_cache/'+widget_name+'.pkl')
                        self.updateMasterDataFrame(
                            master_data_frame, widget_name, user_id, database_id, time_stamp_from, time_stamp_to)
                else:
                    json_widget_data = getWidgetData(database_id, sql_query)
                    widget_data = pd.read_json(json_widget_data)
                    widget_data.to_pickle('panda_cache/'+widget_name+'.pkl')
                    self.addNewRefrenceInMasterDataframe(
                        master_data_frame, widget_name, user_id, database_id, time_stamp_from, time_stamp_to)
        except (Exception) as error:
            print(error)
        finally:
            print('Process completed.')

        return widget_data

    # Load Master Dataframe from Memory
    def loadMasterDataFrame(self):
        try:
            df = pd.read_pickle("panda_cache/master.pkl")
            print(df)
            return df
        except (Exception) as error:
            print(error)
            return None

    # load Cached Data Frames
    def loadCachedDataFrames(self, widget_name):
        try:
            df = pd.read_pickle('panda_cache/'+widget_name+'.pkl')
            print('Cached data retured for '+widget_name)
            return df
        except (Exception) as error:
            print(error)
            return None

    # Create Master Dataframe
    def createMasterDataframe(self):
        try:
            master_data_frame = pd.DataFrame(columns=[
                                             'widget_name', 'user_id', 'database_id', 'time_stamp_from', 'time_stamp_to', 'last_modification_time'])
            master_data_frame.to_pickle('panda_cache/master.pkl')
            return master_data_frame
        except (Exception) as error:
            print(error)
        return None

    # Add refrence of new widget cache in Master Dataframe
    def addNewRefrenceInMasterDataframe(self, master_data_frame, widget_name, user_id, database_id, time_stamp_from, time_stamp_to):
        status = False
        current_date_time = datetime.now()
        try:
            updated_df = master_data_frame.append(pd.DataFrame({'widget_name': [widget_name], 'user_id': [user_id], 'database_id': [database_id], 'time_stamp_from': [
                                                  time_stamp_from], 'time_stamp_to': [time_stamp_to], 'last_modification_time': current_date_time}), ignore_index=True)
            updated_df.to_pickle('panda_cache/master.pkl')
            status = True
        except (Exception) as error:
            print(error)
        return status

    # Update Master Dataframe incase of change in date filters
    def updateMasterDataFrame(self, dataFrameToUpdate, widget_name, user_id, database_id, time_stamp_from, time_stamp_to):
        status = False
        try:
            current_date_time = datetime.now()
            dataFrameToUpdate.loc[(master_data_frame['widget_name'] == widget_name) & (master_data_frame['user_id'] == user_id) & (
                master_data_frame['database_id'] == database_id), 'time_stamp_from'] = time_stamp_from
            dataFrameToUpdate.loc[(master_data_frame['widget_name'] == widget_name) & (master_data_frame['user_id'] == user_id) & (
                master_data_frame['database_id'] == database_id), 'time_stamp_to'] = time_stamp_to
            dataFrameToUpdate.loc[(master_data_frame['widget_name'] == widget_name) & (master_data_frame['user_id'] == user_id) & (
                master_data_frame['database_id'] == database_id), 'last_modification_time'] = current_date_time
            dataFrameToUpdate.to_pickle('panda_cache/master.pkl')
            status = True
        except (Exception) as error:
            print(error)
        return status

    # Get detail of widget cache file from Master Data Frame
    def getWidgetDataFrameRefrence(self, master_data_frame, widget_name, user_id, database_id):
        widget_data_ref = master_data_frame.loc[(master_data_frame['widget_name'] == widget_name) & (
            master_data_frame['user_id'] == user_id) & (master_data_frame['database_id'] == database_id)]
        widget_data_count = widget_data_ref.count().widget_name
        return widget_data_ref

    def jsonloads(self, text):
        index, values = json.loads(text)
        return pd.read_json

    # Create panda SQL query
    def getPandaSqlQuery(self, sql_query, widget_name):
        sql_table_name = extract_tables(sql_query)
        panda_sql_query = sql_query.replace(sql_table_name, widget_name)
        return panda_sql_query
