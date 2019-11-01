from .__widget import __Widget
import plotly.graph_objs as go


class Widget(__Widget):

    # generate data for bar chart
    def get_data(self):
        data_arr = self.config['graph']['data']

        return [
            go.Bar(
                x=data['x'],
                y=data['y'],
                name=data['name'] if 'name' in data else None,
                marker=self.get_marker(data)
            ) for data in data_arr
        ]
