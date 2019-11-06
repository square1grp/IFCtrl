from components.widget_board import get_widget_board


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

        return children

    # get report content
    def get_content_reports(self):
        return 'This is a blank-report'

    # get content
    # widget-baord feeds or reports
    def get_content(self):
        if self.content_type == 'widget-board':
            return self.get_content_widget_boards()

        return self.get_content_reports()
