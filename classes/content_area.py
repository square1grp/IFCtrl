from components.widget_board import get_widget_board
import dash_html_components as html
import dash_bootstrap_components as dbc
from querymanager.intelliflux_dashboard_api_consumer import getWidgetData
import json


# content area class
# this class manages the content(widget-board/report)
class ContentArea:
    content_type = 'widget-board'
    content_data = []

    def __init__(self, page):
        self.content_type = page['content-type']
        self.content_data = page['config']

    # get widget boards content
    def get_content_widget_boards(self):
        children = []

        for widget_board in self.content_data:
            children.append(
                get_widget_board(widget_board['widgets'])
            )

        children.append(self.get_test_table_relativeIntensity())
        return children

    def getrelativeIntensity(self):
        try:
            data = getWidgetData(
                4, 'SELECT relativeIntensity FROM cleans ORDER BY startTime DESC LIMIT 1')

            data = json.loads(data)

            if 'relativeIntensity' not in data or not len(data['relativeIntensity']):
                return ' - '

            return data['relativeIntensity']['0']
        except:
            return ' - '

    # get test table for disply relativeIntensity
    def get_test_table_relativeIntensity(self):
        return dbc.Row(
            dbc.Col(
                html.Div(
                    [html.Div(
                        html.H4('Relative Intensity'),
                        className='title text-uppercase text-center'
                    ), html.Div(
                        html.H2(self.getrelativeIntensity(), className='m-auto'),
                        className='text-uppercase text-center font-weight-bold min-250h d-flex flex-column'
                    )],
                    className='widget relative-intensity-table'
                ),
                className='col-12 col-md-6 col-lg-5 p-md-1'
            )
        )

    # get report content

    def get_content_reports(self):
        return 'This is a blank-report'

    # get content
    # widget-baord feeds or reports
    def get_content(self):
        if self.content_type == 'widget-board':
            return self.get_content_widget_boards()

        return self.get_content_reports()
