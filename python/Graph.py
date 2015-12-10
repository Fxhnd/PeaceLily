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

            



#s0 = Stream(token=stream_ids[0], maxpoints=100)
#s1 = Stream(token=stream_ids[1], maxpoints=100)
#s2 = Stream(token=stream_ids[2], maxpoints=100)
#s3 = Stream(token=stream_ids[3], maxpoints=100)

#t1 = Scatter(x=[], y=[], mode='lines+markers', stream=s0)
#t2 = Scatter(x=[], y=[], mode='lines+markers', stream=s1)
#t3 = Scatter(x=[], y=[], mode='lines+markers', stream=s2)
#t4 = Scatter(x=[], y=[], mode='lines+markers', stream=s3)
#fig = Figure(data=data, layout=layout)


#s_1 = py.Stream(stream_ids[0])
#s_1.open()

#s_2 = py.Stream(stream_ids[1])
#s_2.open()

#s_3 = py.Stream(stream_ids[2])
#s_3.open()

#s_4 = py.Stream(stream_ids[3])
#s_4.open()

#while True:


#    ts = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#    with open('output.csv', 'a') as f:
#        f.write(ts + ' ' + str(data) + '\n')

#    print ts, data

#    s_1.write(dict(x=ts, y=data[0]))
#    s_2.write(dict(x=ts, y=data[1]))
#    s_3.write(dict(x=ts, y=data[2]))
#    s_4.write(dict(x=ts, y=data[3]))

#    time.sleep(1800)

#s_1.close()
#s_2.close()
#s_3.close()
#s_4.close()
print 'potato'
