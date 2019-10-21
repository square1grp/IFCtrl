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


json_data = {
    "nav": [{
        "label": "Page Nav Item 1",
        "target": "/page-1"
    }, {
        "label": "Page Nav Item 2",
        "target": "/page-2"
    }, {
        "label": "Page Nav Item 3",
        "target": "/page-3"
    }, {
        "label": "Page Nav Item 4",
        "target": "/page-4"
    }, {
        "label": "Page Nav Item 5",
        "target": "/page-5"
    }],

    "pages": [{
        "name": "Page Title 1",
        "slug": "page-1",
        "content-type": "widget-board",
        "config": [{
            "widgets": [{
                "size": "medium",
                "type": "mirror",
                "children": [{
                    "config": {
                        "graph_data": get_graph_data("bar1"),
                        "backgroundColor": "#E2D5E6"
                    }
                }, {
                    "config": {
                        "graph_data": get_graph_data("bar2"),
                        "backgroundColor": "#E2D5E6"
                    }
                }]
            }, {
                "size": "medium",
                "config": {
                    "graph_data": get_graph_data("scatter"),
                    "backgroundColor": "#E2D5E6"
                }
            }, {
                "size": "medium",
                "config": {
                    "graph_data": get_graph_data("pie"),
                    "backgroundColor": "#E2D5E6"
                }
            }]
        }, {
            "widgets": [{
                "size": "xlarge",
                "config": {
                    "graph_data": get_graph_data("pie"),
                    "backgroundColor": "#E2D5E6"
                }
            }]
        }, {
            "widgets": [{
                "size": "medium",
                "config": {
                    "graph_data": get_graph_data("scatter"),
                    "backgroundColor": "#E2D5E6"
                }
            }, {
                "size": "large",
                "config": {
                    "graph_data": get_graph_data("scatter"),
                    "backgroundColor": "#E2D5E6"
                }
            }]
        }]
    }, {
        "name": "Page Title 2",
        "slug": "page-2",
        "content-type": "widget-board",
        "config": [{
            "widgets": [{
                "size": "medium",
                "config": {
                    "graph_data": get_graph_data("bar1"),
                    "backgroundColor": "#E2D5E6"
                }
            }, {
                "size": "large",
                "config": {
                    "graph_data": get_graph_data("bar2"),
                    "backgroundColor": "#E2D5E6"
                }
            }]
        }, {
            "widgets": [{
                "size": "medium",
                "config": {
                    "graph_data": get_graph_data("scatter"),
                    "backgroundColor": "#E2D5E6"
                }
            }, {
                "size": "large",
                "config": {
                    "graph_data": get_graph_data("pie"),
                    "backgroundColor": "#E2D5E6"
                }
            }]
        }, {
            "widgets": [{
                "size": "xlarge",
                "config": {
                    "graph_data": get_graph_data("pie"),
                    "backgroundColor": "#E2D5E6"
                }
            }]
        }]
    }, {
        "name": "Page Title 3",
        "slug": "page-3",
        "content-type": "widget-board",
        "config": [{
            "widgets": [{
                "size": "xlarge",
                "config": {
                    "graph_data": get_graph_data("pie"),
                    "backgroundColor": "#E2D5E6"
                }
            }]
        }, {
            "widgets": [{
                "size": "medium",
                "config": {
                    "graph_data": get_graph_data("pie"),
                    "backgroundColor": "#E2D5E6"
                }
            }, {
                "size": "large",
                "config": {
                    "graph_data": get_graph_data("pie"),
                    "backgroundColor": "#E2D5E6"
                }
            }]
        }, {
            "widgets": [{
                "size": "medium",
                "config": {
                    "graph_data": get_graph_data("pie"),
                    "backgroundColor": "#E2D5E6"
                }
            }, {
                "size": "large",
                "config": {
                    "graph_data": get_graph_data("pie"),
                    "backgroundColor": "#E2D5E6"
                }
            }]
        }]
    }, {
        "name": "Page Title 4",
        "slug": "page-4",
        "content-type": "widget-board",
        "config": [{
            "widgets": [{
                "size": "xlarge",
                "config": {
                    "graph_data": get_graph_data("pie"),
                    "backgroundColor": "#E2D5E6"
                }
            }]
        }, {
            "widgets": [{
                "size": "medium",
                "config": {
                    "graph_data": get_graph_data("pie"),
                    "backgroundColor": "#E2D5E6"
                }
            }, {
                "size": "large",
                "config": {
                    "graph_data": get_graph_data("pie"),
                    "backgroundColor": "#E2D5E6"
                }
            }]
        }, {
            "widgets": [{
                "size": "xlarge",
                "config": {
                    "graph_data": get_graph_data("pie"),
                    "backgroundColor": "#E2D5E6"
                }
            }]
        }, {
            "widgets": [{
                "size": "medium",
                "config": {
                    "graph_data": get_graph_data("pie"),
                    "backgroundColor": "#E2D5E6"
                }
            }, {
                "size": "large",
                "config": {
                    "graph_data": get_graph_data("pie"),
                    "backgroundColor": "#E2D5E6"
                }
            }]
        }]
    }, {
        "name": "Page Title 5",
        "slug": "page-5",
        "content-type": "widget-board",
        "config": [{
            "widgets": [{
                "size": "xlarge",
                "config": {
                    "graph_data": get_graph_data("pie"),
                    "backgroundColor": "#E2D5E6"
                }
            }]
        }, {
            "widgets": [{
                "size": "xlarge",
                "config": {
                    "graph_data": get_graph_data("pie"),
                    "backgroundColor": "#E2D5E6"
                }
            }]
        }, {
            "widgets": [{
                "size": "medium",
                "config": {
                    "graph_data": get_graph_data("pie"),
                    "backgroundColor": "#E2D5E6"
                }
            }, {
                "size": "large",
                "config": {
                    "graph_data": get_graph_data("pie"),
                    "backgroundColor": "#E2D5E6"
                }
            }]
        }, {
            "widgets": [{
                "size": "medium",
                "config": {
                    "graph_data": get_graph_data("pie"),
                    "backgroundColor": "#E2D5E6"
                }
            }, {
                "size": "large",
                "config": {
                    "graph_data": get_graph_data("pie"),
                    "backgroundColor": "#E2D5E6"
                }
            }]
        }]
    }]
}
