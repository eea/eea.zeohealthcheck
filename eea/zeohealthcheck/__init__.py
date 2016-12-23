""" Check database connection
"""
from App.ApplicationManager import ApplicationManager

def health_check(self):
    """ Checks if there is an active connection between the client
        and zeo server.
    """
    if context._p_jar.db().storage.is_connected():
        return self.REQUEST.RESPONSE.setStatus('OK')
    else:
        return self.REQUEST.RESPONSE.setStatus('ServiceUnavailable')

ApplicationManager.health_check = health_check
