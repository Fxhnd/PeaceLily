"""
@Author Robert Powell
@Module PeaceLilly
@Version 1.0.0
"""

import serial
import datetime
import argparse
import time
#import plotly.plotly as py
#import plotly.tools as tls
#from plotly.graph_objs import *

def get_serial_connection(port):
    """
    Return a serial connection to a given port. Raise an exception if given port
    isn't accessible.

    :param str port: Port
    :return Python serial connection
    :rtype: serial object
    """

    try:

        conn = serial.Serial(port, 9600, timeout=5)
        return conn

    except serial.SerialException:

        print 'Could not connect to serial device!'
        print 'Please check that the proper port setting is used.'
        exit(1)

def _query(conn):
    """
    Query the Arduino for a new data tuple. If success return the tuple,
    otherwise return empty tuple.

    :param object conn: Connection
    :return temperature, humitidy, lux, and soil-moisture
    :rtype tuple
    """

    _request_tuple(conn)
    return _read_tuple(conn)



def _request_tuple(conn):
    """
    Send a command sequence to the Arduino to return a new tuple. If sucess
    returns True, otherwise False.

    :param object conn: Connection
    :return status of request
    :rtype bool
    """

    try:

        conn.write('r\n')
        return True

    except serial.SerialTimeoutException:

        print 'Error writing to device!'
        return False


def _read_tuple(conn):
    """
    Read a message from the serial connection. If success then return tuple,
    otherwise return empty tuple on timeout.

    :param object conn: Connection
    :return data from Arduino
    :rtype tuple
    """

    try:

        msg = conn.readline()
        data = tuple(msg.strip().split(','))
        return data

    except serial.SerialTimeoutException:

        print 'Serial read timeout!'
        return ()

def _process_msg(msg):
    """
    Add a timestamp to a given tuple and convert types of return values.

    :param tuple msg: Message from Arduino
    :return A normalized tuple for storage
    :rtype tuple
    """

    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    if msg == () or msg == ('',):
        return (timestamp, -1, -1, -1, -1)

    return tuple([timestamp] + [float(x) for x in msg])


def get_data(conn):
    """
    Retrieve a new data tuple from the Arduino. Return normalized tuple for
    storage and processing.

    :param object conn: Connection
    :return A normalized tuple to store
    :rtype tuple
    """

    new_data = _query(conn)
    norm_tuple = _process_msg(new_data)

    return norm_tuple

def setup(port):
    """
    Establish a serial object and return it

    :return object A serial object
    :rtupe serial.Serial
    """

    conn = get_serial_connection(port)
    return conn

def loop(conn):
    """
    Begin the polling loop for Arduino data

    :param object conn: Connection
    :return None
    """

    while True:

        time.sleep(5)

        print get_data(conn)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Monitor your plants!')
    parser.add_argument('--port', dest='port', type=str, required=True, \
            help='Serial port connection to arduino')
    parser.add_argument('--file', dest='file', type=str, \
            help='Local file to save result data')

    args = parser.parse_args()

    connection = setup(args.port)
    loop(connection)





    #tls.set_credentials_file(stream_ids=["67ldjwqppe", "hyinh0zrb1",
    #"t4tqyzk86o", "66qg05p8s9", "zbl5fi5amr"])

    #stream_ids = tls.get_credentials_file()['stream_ids']

    #s0 = Stream(token=stream_ids[0], maxpoints=100)
    #s1 = Stream(token=stream_ids[1], maxpoints=100)
    #s2 = Stream(token=stream_ids[2], maxpoints=100)
    #s3 = Stream(token=stream_ids[3], maxpoints=100)

    #t1 = Scatter(x=[], y=[], mode='lines+markers', stream=s0)
    #t2 = Scatter(x=[], y=[], mode='lines+markers', stream=s1)
    #t3 = Scatter(x=[], y=[], mode='lines+markers', stream=s2)
    #t4 = Scatter(x=[], y=[], mode='lines+markers', stream=s3)
    #fig = Figure(data=data, layout=layout)

    #unique_uql = py.plot(fig, filename='PeaceLilly')

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
