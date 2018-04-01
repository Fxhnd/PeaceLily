"""
@Author Robert Powell
@Module PeaceLilly

A simple interface to send email reminders. Should work with any imap enabled
system
"""

import smtplib


class Emailer(object):
    """
    Emailer class to send notifications.
    """

    def __init__(self, username, password, server):
        
        self.username = username
        self.password = password
        self.server = server

        self.server = self._connect_to_server(username, password, server)
        

    def _connect_to_server(self, username, password, server):
        """
        Establish a connection to a mail server. Return the connection if
        success otherwise raise an error
        
        :param str username
        :param str password
        :param str server
        :return An active connection
        :rtype object Connection
        """


        server = smtplib.SMTP(server)
        server.starttls()

        try:

            server.login(username,password)
            return server

        except smtplib.SMTPAuthenticationError as error:

            print 'Error authenticating to server!'
            print 'You may need to set an application password.'
            print 'https://security.google.com/settings/security/apppasswords'

            exit(1)

    def _build_headers(self):
        """
        Private method to stub out an email in proper format

        :return A properly formatted email
        :rtype list
        """

        msg = "\r\n".join([
            "From: " + self.username,
            "To: " + self.username,
            "Subject: PeaceLily Update",
            "",
        ])

        return msg

    def send_mail(self, message):
        """
        Send a email to your signed in account with the provided message.

        :param str message 
        :return None
        :rtype None
        """

        email = self._build_headers()
        email += "\r\n"
        email += message
        self.server.sendmail(self.username, self.username, email)
