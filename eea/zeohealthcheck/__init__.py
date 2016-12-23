""" Check database connection
"""

from Products.Five.browser import BrowserView


class HealthCheck(BrowserView):
    """
    """

    def __call__(self):
        """ Checks if there is an active connection between the client
            and zeo server.
        """
        if self.context._p_jar.db().storage.is_connected():
            return self.request.RESPONSE.setStatus('OK')
        else:
            return self.request.RESPONSE.setStatus('ServiceUnavailable')
