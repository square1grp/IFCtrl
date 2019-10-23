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


def get_graph_data(graph_type):
    if graph_type == 'scatter':
        # modes = ['lines', 'markers', 'lines+markers']

        return [{
            'x': [i for i in range(5)],
            'y': [random.randint(0, 2) for i in range(5)],
            'mode': 'lines+markers',  # modes[random.randint(1, 3) % 3]
            'type': graph_type
        } for j in range(2)]

    if 'bar' in graph_type:

        return [{
            'x': ['Los Angeles', 'Washington', 'Las Vegas'],
            'y': [random.randint(-2, 2) for i in range(3)] if graph_type == 'bar1' else [random.randint(1, 5) for i in range(3)],
            'type': 'bar'
        } for j in range(2)]

    if graph_type == 'pie':
        return [{
            'labels': ['Oxygen', 'Hydrogen', 'Carbon_Dioxide', 'Nitrogen'],
            'values': [random.randrange(10, 45) * 100 for i in range(4)],
            'type': 'pie'
        }]


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
                    "backgroundColor": "#E2D5E6"
                }
            }]
        }, {
            "widgets": [{
                "size": "xlarge",
                "type": "xl-scatter",
                "config": {
                    "backgroundColor": "#E2D5E6"
                }
            }]
        }, {
            "widgets": [{
                "size": "medium",
                "type": "md-scatter",
                "config": {
                    "backgroundColor": "#E2D5E6"
                }
            }, {
                "size": "large",
                "type": "lg-scatter",
                "config": {
                    "backgroundColor": "#E2D5E6"
                }
            }]
        }]
    }]
}
