"""
@Author Robert Powell
@Module PeaceLilly

A simple configuration to push data to plotly for visualization
"""

import plotly.plotly as py
import plotly.tools as tls
from plotly.graph_objs import *

class Graph(object):
    """
    An optional little bit to push data to Plotly.com for a quick visualization.
    """

    def __init__(self):

        tls.set_credentials_file(stream_ids=["67ldjwqppe", "hyinh0zrb1", \
                                 "t4tqyzk86o", "66qg05p8s9", "zbl5fi5amr"])

        stream_ids = tls.get_credentials_file()['stream_ids']

        streams = []
        traces = []

        for i in range(4):

            streams.append(Stream(token=stream_ids[i], maxpoints = 100))

            traces.append(Scatter(x=[], y=[], mode='lines+markers', \
                    stream=streams[i]))


        layout = Layout(title='PeaceLily')
        data = Data(traces)
        fig = Figure(data=data, layout=layout)

        unique_uql = py.plot(fig, filename='PeaceLilly')

        self.active_streams = []

        for i in range(4):
            self.active_streams.append(py.Stream(stream_ids[i]))
            self.active_streams[-1].open()

    def upload_data(self, tup):
        """
        Gonna document this later
        """

        for i in range(0, 4):
            self.active_streams[i].write(dict(x=tup[0], y=tup[i+1]))
