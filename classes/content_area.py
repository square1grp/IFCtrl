from components.widget_board import get_widget_board

import dash_bootstrap_components as dbc
import dash_html_components as html


class ContentArea:
    content_type = 'widget-board'
    content_data = []

    def __init__(self, page):
        self.content_type = page['content-type']
        self.content_data = page['config']

    def get_content_widget_boards(self):
        children = []

        for widget_board in self.content_data:
            children.append(
                get_widget_board(widget_board['widgets'])
            )

        return children

    def get_content_reports(self):
        return 'This is a blank-report'

    def get_content(self):
        if self.content_type == 'widget-board':
            return self.get_content_widget_boards()

        return self.get_content_reports()
