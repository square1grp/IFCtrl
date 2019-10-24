import random

colors = {
    "black":    "#000000",
    "white":    "#FFFFFF",
    "beige":    "#F5F5DC",
    "green":    "#D4E8D5",
    "blue":     "#D8EAFA",
    "yellow":   "#FdF1D0",
    "purple":   "#E2D5E6"
}


# create mockup data
def get_graph(graph_type):
    layout = {
        'title': {
            'text': 'US City',
            'pos_x': 0.5,
            'pos_y': 0.9
        },
        'showLegend': True,
        'legend': {
            'pos_x': 0,
            'pos_y': 1.0
        },
        'margin': {
            'left': 30,
            'right': 10,
            'top': 50,
            'bottom': 30
        }
    }

    if "bar" in graph_type:
        return {
            'data': [{
                'x': ['Los Angeles', 'Washington', 'Las Vegas'],
                'y': [random.randint(1, 5) for i in range(3)],
                'name': 'City',
                'color': 'rgb(%s, %s, %s)' % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            }],
            'layout': layout
        }

    if "scatter" in graph_type:
        return {
            'data': [{
                'x': [i+1 for i in range(15)],
                'y': [random.randint(50, 200) for i in range(15)],
                'mode': 'lines+markers',  # 'lines', 'markers', 'lines+markers'
                'name': 'City',
                'color': 'rgb(%s, %s, %s)' % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            } for j in range(2)],
            'layout': layout
        }


json_data = {
    "nav": [{
        "label": "Page Nav Item 1",
        "target": "/page-1"
    }, {
        "label": "Page Nav Item 2",
        "target": "/page-1"
    }, {
        "label": "Page Nav Item 3",
        "target": "/page-1"
    }, {
        "label": "Page Nav Item 4",
        "target": "/page-1"
    }, {
        "label": "Page Nav Item 5",
        "target": "/page-1"
    }],

    "pages": [{
        "name": "Page Title 1",
        "slug": "page-1",
        "content-type": "widget-board",
        "config": [{
            "widgets": [{
                "size": "medium",
                "layout": "mirror",
                "children": [{
                    "type": "sm-bar",
                    "config": {
                        "graph": get_graph("sm-bar"),
                        "backgroundColor": "#E2D5E6"
                    }
                }, {
                    "type": "sm-bar",
                    "config": {
                        "graph": get_graph("sm-bar"),
                        "backgroundColor": "#E2D5E6"
                    }
                }]
            }, {
                "size": "medium",
                "type": "md-scatter",
                "config": {
                    "graph": get_graph("md-scatter"),
                    "backgroundColor": "#E2D5E6"
                }
            }, {
                "size": "medium",
                "type": "md-scatter",
                "config": {
                    "graph": get_graph("md-scatter"),
                    "backgroundColor": "#E2D5E6"
                }
            }]
        }, {
            "widgets": [{
                "size": "xlarge",
                "type": "xl-scatter",
                "config": {
                    "graph": get_graph("xl-scatter"),
                    "backgroundColor": "#E2D5E6"
                }
            }]
        }, {
            "widgets": [{
                "size": "medium",
                "type": "md-scatter",
                "config": {
                    "graph": get_graph("md-scatter"),
                    "backgroundColor": "#E2D5E6"
                }
            }, {
                "size": "large",
                "type": "lg-scatter",
                "config": {
                    "graph": get_graph("lg-scatter"),
                    "backgroundColor": "#E2D5E6"
                }
            }]
        }]
    }]
}
