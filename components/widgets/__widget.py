import dash_html_components as html


# widget abstract class
class __Widget:
    is_child_widget = False
    widget_type = None

    # set config
    def __init__(self, config, widget_type, is_child_widget=False):
        self.config = config
        self.widget_type = widget_type
        self.is_child_widget = is_child_widget

    # get marker options
    def get_data_marker(self, data=dict(), marker_props=[], color_key=None):
        go_marker = dict()

        if 'marker' not in data:
            return go_marker

        for prop in marker_props:
            if prop in data['marker']:
                go_marker[prop] = data['marker'][prop]

                if prop == 'colorscale' and color_key in data:
                    go_marker['color'] = data[color_key]

        return go_marker

    # return graph layout
    def get_graph_layout(self, options=dict()):
        try:
            layout = self.config['graph']['layout']
        except:
            layout = dict()

        go_layout = dict()

        for key in ['title', 'xaxis', 'yaxis', 'showlegend']:
            if key in layout:
                go_layout[key] = layout[key]

        go_layout['paper_bgcolor'] = 'rgba(0,0,0,0)'
        go_layout['plot_bgcolor'] = 'rgba(0,0,0,0)'

        go_layout['height'] = 300 if 'xl-' in self.widget_type else 250
        go_layout['margin'] = dict(b=40, t=40, r=30)

        go_layout.update(options)

        return go_layout

    # get title area
    def get_widget_title(self, title):
        return html.Div(
            html.H4(title['text'] if 'text' in title else ''),
            className='title %s' % (
                ('text-%s' % title['transform']) if 'transform' in title
                else ''
            )
        )

    # get graph in the current widget
    def get_widget_graph(self):
        return []

    # content which draws a widget
    # default: colored rect range
    def get_content(self):
        widget_content = []

        if 'title' in self.config:
            widget_content.append(self.get_widget_title(self.config['title']))

        for graph in self.get_widget_graph():
            widget_content.append(graph)

        return html.Div(
            widget_content,
            className='widget %s' % (self.widget_type)
        )
