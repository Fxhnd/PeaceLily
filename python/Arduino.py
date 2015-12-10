"""
@Author Robert Powell
@Module PeaceLilly
@Class Arduino

Provides a simple API to extract data in a normalized form from the
Arduino.
"""

import serial
import datetime

class Arduino(object):
    """
    A convenience class to provide an API into the arduino
    """

    def __init__(self, port):

        self.conn = self.conn = self._setup(port)

    def get_serial_connection(self, port):
        """
        Return a serial connection to a given port. Raise an exception if given
        port isn't accessible.

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

    def _query(self, conn):
        """
        Query the Arduino for a new data tuple. If success return the tuple,
        otherwise return empty tuple.

        :param object conn: Connection
        :return temperature, humitidy, lux, and soil-moisture
        :rtype tuple
        """

        self._request_tuple(conn)
        return self._read_tuple(conn)

    def _request_tuple(self, conn):
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

    def _read_tuple(self, conn):
        """
        Read a message from the serial connection. If success then return tuple,
        otherwise return empty tuple on timeout.

        :param object conn: Connection
        :return data from Arduino
        :rtype tuple
        """

        try:

            msg = conn.readline()
            data = msg.strip().split(',')

            if data == ['']:
                return ()
            else:
                return tuple(data)

        except serial.SerialTimeoutException:

            print 'Serial read timeout!'
            return ()

    def _process_msg(self, msg):
        """
        Add a timestamp to a given tuple and convert types of return values.

        :param tuple msg: Message from Arduino
        :return A normalized tuple for storage
        :rtype tuple
        """

        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        if msg == () or msg == (''):
            return (timestamp, -1, -1, -1, -1)


        return tuple([timestamp] + [float(x) for x in msg])


    def get_data(self):
        """
        Retrieve a new data tuple from the Arduino. Return normalized tuple for
        storage and processing.

        :param object conn: Connection
        :return A normalized tuple to store
        :rtype tuple
        """

        new_data = self._query(self.conn)
        norm_tuple = self._process_msg(new_data)

        return norm_tuple

    def _setup(self, port):
        """
        Establish a serial object and return it

        :return object A serial object
        :rtupe serial.Serial
        """

        conn = self.get_serial_connection(port)
        return conn
