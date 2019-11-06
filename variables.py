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
                            "x": ['4/1', '4/2', '4/3', '4/4', '4/5', '4/6', '4/7', '4/8', '4/9', '4/10', '4/11', '4/12', '4/13', '4/14', '4/15', '4/16', '4/17', '4/18', '4/19', '4/20', '4/21', '4/22', '4/23', '4/24', '4/25', '4/26', '4/27', '4/28', '4/29', '4/30', '4/31'],
                            "y": [29843, 10683, 17465, 15806, 0, 18005, 20119, 10075, 28289, 0, 15254, 25542, 25577, 11331, 0, 0, 24202, 24981, 0, 26281, 0, 0, 22403, 17844, 0, 0, 0, 29883, 16626, 10058, 0],
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
                            "x": ['4/1', '4/2', '4/3', '4/4', '4/5', '4/6', '4/7', '4/8', '4/9', '4/10', '4/11', '4/12', '4/13', '4/14', '4/15', '4/16', '4/17', '4/18', '4/19', '4/20', '4/21', '4/22', '4/23', '4/24', '4/25', '4/26', '4/27', '4/28', '4/29', '4/30', '4/31'],
                            "y": [0.31, 0.48, 0.76, 0.68, 0.83, 0.42, 0.31, 0.83, 0.78, 0.55, 0.73, 0.61, 0.82, 0.85, 0.77, 0.74, 0.34, 0.46, 0.44, 0.48, 0.87, 0.45, 0.7, 0.76, 0.56, 0.8, 0.39, 0.8, 0.49, 0.99, 0.41],
                            "line": {
                                "color": "#FF0000"
                            }
                        }, {
                            "x": ['4/1', '4/2', '4/3', '4/4', '4/5', '4/6', '4/7', '4/8', '4/9', '4/10', '4/11', '4/12', '4/13', '4/14', '4/15', '4/16', '4/17', '4/18', '4/19', '4/20', '4/21', '4/22', '4/23', '4/24', '4/25', '4/26', '4/27', '4/28', '4/29', '4/30', '4/31'],
                            "y": [-0.25, -0.04, -0.18, -0.01, -0.07, -0.06, -0.3, -0.09, -0.05, -0.29, -0.27, -0.1, -0.19, -0.05, -0.3, -0.06, -0.28, -0.03, -0.15, -0.27, -0.09, -0.24, -0.1, -0.17, -0.17, -0.17, -0.26, -0.21, -0.04, -0.17, -0.2],
                            "fill": "tonexty",
                            "line": {
                                "color": "#FF9A00"
                            }
                        }],
                        "show_average": True,
                        "layout": {
                            "showlegend": False,
                            "xaxis": {
                                "tickvals": ['4/1', '4/8', '4/15', '4/22', '4/29'],
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
                            "labels": ['4/1', '4/6', '4/11', '4/16', '4/21', '4/26', '4/31'],
                            "values": [37, 13, 15, 27, 40, 27],
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
