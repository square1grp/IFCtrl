from random import randint, uniform

colors = {
    "black":    "#000000",
    "white":    "#FFFFFF",
    "beige":    "#F5F5DC",
    "green":    "#D4E8D5",
    "blue":     "#D8EAFA",
    "yellow":   "#FdF1D0",
    "purple":   "#E2D5E6"
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
                "size": "xlarge",
                "type": "xl-bar",
                "config": {
                    "title": {
                        "text": "Production Volume Trend",
                        "transform": "uppercase",
                    },
                    "graph": {
                        "data": [{
                            "x": ["4/%s" % date for date in range(1, 32)],
                            "y": [value if value > 10000 else 0 for value in [randint(5000, 30000) for i in range(31)]],
                            "marker": {
                                "colorscale": [
                                    [0.0, "#AAAAFF"],
                                    [0.3, "#8989FF"],
                                    [0.7, "#0101FF"],
                                    [1.0, "#0000FF"]
                                ],
                                "line_color": "#009900",
                                "line_width": 1.5,
                                "showscale": True,
                                "colorbar": {
                                    "len": 1.1,
                                    "tickvals": [5000, 10000, 15000, 20000, 25000],
                                    "ticktext": ["5,000", "10,000", "15,000", "20,000", "25,000"],
                                    "outlinewidth": 0
                                }
                            }
                        }],
                        "layout": {
                            "showlegend": False,
                            "xaxis": {
                                "tickfont_color": "#000000",
                                "showgrid": True,
                                "zeroline": True,
                                "gridcolor": "#5F5F5F",
                                "showline": True,
                                "linewidth": 2,
                                "linecolor": "#5F5F5F"
                            },
                            "yaxis": {
                                "title": "Gallons Produced",
                                "title_font_color": "#000000",
                                "ticktext": ['0', '10,000', '20,000', '30,000'],
                                "tickvals": [0, 10000, 20000, 30000],
                                "tickfont_color": "#000000",
                                "showgrid": True,
                                "gridcolor": "#5F5F5F",
                                "showline": False
                            }
                        }
                    }
                }
            }]
        }, {
            "widgets": [{
                "size": "medium",
                "type": "md-scatter",
                "config": {
                    "title": {
                        "text": "TMP Daily Range",
                        "transform": "uppercase"
                    },
                    "graph": {
                        "data": [{
                            "x": ["4/%s" % date for date in range(1, 32)],
                            "y": [uniform(0.3, 1) for i in range(31)],
                            "line": {
                                "color": "#FF0000"
                            }
                        }, {
                            "x": ["4/%s" % date for date in range(1, 32)],
                            "y": [uniform(-0.3, 0) for i in range(31)],
                            "fill": "tonexty",
                            "line": {
                                "color": "#FF9A00"
                            }
                        }],
                        "show_average": True,
                        "layout": {
                            "showlegend": False,
                            "xaxis": {
                                "tickvals": ["4/%s" % date for date in range(1, 32) if date % 7 == 1],
                                "tickfont_color": "#000000",
                                "showgrid": True,
                                "zeroline": True,
                                "gridcolor": "#5F5F5F",
                                "showline": True,
                                "linewidth": 2,
                                "linecolor": "#5F5F5F"
                            },
                            "yaxis": {
                                "title": "Bar",
                                "tickvals": [-0.5, 0, 0.5, 1],
                                "ticktext": ['-0.5', '0', '0.5', '1.0'],
                                "tick0": -0.5,
                                "tickfont_color": "#000000",
                                "showgrid": True,
                                "gridcolor": "#5F5F5F",
                                "showline": False,
                                "zerolinecolor": "#5F5F5F",
                                "zerolinewidth": 1
                            }
                        }
                    }
                }
            }, {
                "size": "medium",
                "type": "md-pie",
                "config": {
                    "title": {
                        "text": "High Frequency Cleans",
                        "transform": "uppercase"
                    },
                    "graph": {
                        "data": [{
                            "labels": ["4/%s" % date for date in range(1, 32) if date % 5 == 1],
                            "values": [randint(1, 40) for i in range(6)],
                            "marker": {
                                "colors": [
                                    "#4747FF",
                                    "#00AC00",
                                    "#00D900",
                                    "#AC5F00",
                                    "#FFAC47",
                                    "#FF8C00"
                                ]
                            }
                        }],
                        "layout": {
                            "showlegend": False,
                        }
                    }
                }
            }]
        }, {
            "widgets": [{
                "size": "xlarge",
                "type": "xl-gauge",
                "config": {
                    "title": {
                        "text": "Baseline Comparison",
                        "transform": "uppercase"
                    },
                    "graph": {}
                }
            }]
        }]
    }]
}
