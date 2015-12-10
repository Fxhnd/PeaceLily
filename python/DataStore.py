"""
@Author Robert Powell
@Module PeaceLilly
@Class Datastore

Provides utility class to handling saving data to a local storage medium.
Default medium is a local sqllite3 container.
"""

import sqlite3

class Datastore(object):
    """
    API wrapper for saving data to local database
    """

    def __init__(self, filename):

        self.filename = filename
        self.conn = self._get_sqlite_connection(filename)

        self._setup_table_schema(self.conn)


    def _get_sqlite_connection(self, filename):
        """
        Open a connection to a sqlite3 database. Return the connection otherwise
        raise an exception

        :param str filename: Filename of local file
        :return object
        :rtype ?
        """

        conn = sqlite3.connect(filename)

        return conn

    def _setup_table_schema(self, conn):
        """
        Check to make sure correct table structure is in place in opened
        storage. If tables are missing, create them otherwise pass

        :param object conn: Connection
        :return Status of tables
        :rtype bool
        """

        conn.execute('CREATE TABLE IF NOT EXISTS records ( \
                id INTEGER PRIMARY KEY AUTOINCREMENT, \
                timestamp TEXT, \
                temp REAL, \
                humid REAL, \
                moist INTEGER, \
                lux INTEGER \
                );')

        return True

    def insert_new_data(self, data):
        """
        Take a tuple of data and insert it into the local database. Return True
        is operation success, otherwise return False

        :param tuple data: (timestamp, temp, humid, moist, lux)
        :return Success status of insertion
        :rtype bool
        """

        try:

            self.conn.execute('INSERT INTO records \
                    (timestamp, temp, humid, moist, lux) \
                    VALUES \
                    (?, ?, ?, ?, ?)', data)

            return True

        except sqlite3.Error as error:
            # TODO get specific exceptions for insert errors

            print 'Failed to insert record with error:', error
            return False
