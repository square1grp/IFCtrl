from variables import colors
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import plotly.graph_objs as go


# widget abstract class
class __Widget:
    is_child_widget = False
    widget_type = None

    # set config
    def __init__(self, config, widget_type, is_child_widget=False):
        self.config = config
        self.widget_type = widget_type
        self.is_child_widget = is_child_widget
    
    # get keys of graph_obj
    def get_attr_key_list(self, attr_type):
        if 'bar' in self.widget_type:
            if attr_type == 'layout':
                return ['title', 'xaxis', 'yaxis', 'showlegend']
            elif attr_type == 'marker':
                return ['colorscale', 'line_color', 'line_width', 'showscale', 'colorbar']
    
        return []
    
    # get marker
    def get_marker(self, data):
        go_marker = dict()

        if 'marker' not in data:
            return go_marker
        
        if 'colorscale' in data['marker']:
            go_marker['color'] = data['y']
        
        for key in self.get_attr_key_list('marker'):
            if key in data['marker']:
                go_marker[key] = data['marker'][key]
        
        return go_marker
        
    # get title area
    def get_title(self, title):
        return html.Div(
            html.H4(title['text'] if 'text' in title else ''),
            className='title %s' % ('text-%s' % title['transform']) if 'transform' in title else None
        )

    # return graph data
    def get_data(self):
        return None

    # return graph layout
    def get_layout(self):
        layout = self.config['graph']['layout']

        go_layout = dict()

        for key in self.get_attr_key_list('layout'):
            if key in layout:
                go_layout[key] = layout[key]

        go_layout['paper_bgcolor'] = 'rgba(0,0,0,0)'
        go_layout['plot_bgcolor'] = 'rgba(0,0,0,0)'
        return go_layout

    # content which draws a widget
    # default: colored rect range 
    def get_content(self):
        widget_content = []

        if 'title' in self.config:
            widget_content.append(self.get_title(self.config['title']))
        
        widget_content.append(
            dcc.Graph(
                figure=go.Figure(
                    data=self.get_data(),
                    layout=self.get_layout()
                ),
                className='m-auto'
            )
        )

        return html.Div(
            widget_content,
            className='widget'
        )
