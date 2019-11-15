import dash_bootstrap_components as dbc
from importlib import import_module


# get class names
def get_classNames(size):
    if size == "xlarge":
        return None

    if size == "large":
        return 'col-xl-9'

    if size == "medium":
        return 'col-xl-6 col-lg-8'

    return 'col-xl-3 col-lg-4 col-md-6'


# create wdiget board
def get_widget_board(widgets):
    children = []

    for widget in widgets:
        # check if widget is mirror layout which shows 2 widgets
        if 'layout' in widget and widget['layout'] is 'mirror':
            mirror_children = []

            for idx, child_widget in enumerate(widget['children'], start=1):
                Widget = getattr(import_module(
                    'components.widgets.%s' % child_widget['type'].replace('-', '.')), 'Widget')

                ele_widget = Widget(
                    child_widget['config'], child_widget['type'], True)

                mirror_children.append(
                    dbc.Col(
                        ele_widget.get_content(),
                        className='col-12 %s child-widget-container p-0' %
                        ('' if idx == len(widget['children']) else 'mb-2')
                    )
                )

            children.append(
                dbc.Col(
                    dbc.Row(
                        mirror_children,
                        className='mx-auto'
                    ),
                    className='col-12 mb-2 widget-container px-lg-5 %s' % get_classNames(
                        widget['size'])
                )
            )
        # widget which is not mirror layouted
        else:
            Widget = getattr(import_module('components.widgets.%s' %
                                           widget['type'].replace('-', '.')), 'Widget')
            ele_widget = Widget(widget['config'], widget['type'])

            children.append(
                dbc.Col(
                    ele_widget.get_content(),
                    className='col-12 mb-2 widget-container px-lg-5 %s' % get_classNames(
                        widget['size'])
                )
            )

    # add widgets to the widget board
    board_feed = dbc.Row(
        children,
        className="widget-board"
    )

    return board_feed
