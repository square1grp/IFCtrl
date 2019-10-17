from components.widget import Widget

import dash_bootstrap_components as dbc
import dash_html_components as html


def get_widget_board(widgets):
    children = []

    for widget in widgets:
        if 'type' in widget and widget['type'] is 'mirror':
            mirror_children = []

            for idx, child_widget in enumerate(widget['children'], start=1):
                ele_widget = Widget(child_widget['config'], True)

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
                    className='col-12 %s mb-2 widget-container p-md-1'
                    % ('col-md-4' if widget['size'] == 'medium' else ('col-md-8' if widget['size'] == 'large' else ''))
                )
            )
        else:
            ele_widget = Widget(widget['config'])

            children.append(
                dbc.Col(
                    ele_widget.get_content(),
                    className='col-12 %s mb-2 widget-container p-md-1'
                    % ('col-md-4' if widget['size'] == 'medium' else ('col-md-8' if widget['size'] == 'large' else ''))
                )
            )

    board_feed = dbc.Row(
        children,
        className="widget-board"
    )

    return board_feed
