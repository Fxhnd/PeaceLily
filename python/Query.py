"""
@Author Robert Powell
@Module PeaceLilly
@Class Main
"""

import argparse
import time
import Arduino
import DataStore
import Graph
import Stats


class Main(object):
    """
    Running class for the whole program
    """

    def __init__(self, port, opts):

        self.arduino = Arduino.Arduino(port)
        self.filename = opts['file']
        self.opts = opts
        self.graph = Graph.Graph()

        if opts['file']:
            self.store = DataStore.Datastore(opts['file'])

        self.loop()
        self.emailer = Emailer(opts['user'], opts['pass'], 'smtp.gmail.com:587')


    def loop(self):
        """
        Begin the polling loop for Arduino data

        :param object conn: Connection
        :return None
        """

        while True:

            data = self.arduino.get_data()
            print data

            if self.store:
                self.store.insert_new_data(data)

            days_left = Stats.calculate_ttnw(data[4])

            if days_left > 0:
                self.emailer.send_mail(str(days_left) + ' until next watering!')
            else:
                self.emailer.send_mail('Water your plant TODAY!')

            self.graph.upload_data(data)
            time.sleep(float(self.opts['time']))


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Monitor your plants!')

    parser.add_argument('--port', dest='port', type=str, required=True, \
            help='Serial port connection to arduino')

    parser.add_argument('--file', dest='file', type=str, \
            help='Local file to save result data')

    parser.add_argument('--time', dest='time', type=str, \
            help='Interval time for polling for new data')

    parser.add_argument('--user', dest='user', type=str, \
            help='Username for email account')

    parser.add_argument('--pass', dest='user', type=str, \
            help='Password for email account')

    args = vars(parser.parse_args())

    app = Main(args['port'], args)
