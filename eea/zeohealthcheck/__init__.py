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
        db = self.context.Control_Panel.Database.__getitem__(
            'temporary')._p_jar.db().storage
        if db.is_connected():
            return self.request.RESPONSE.setStatus('OK')
        else:
            return self.request.RESPONSE.setStatus('ServiceUnavailable')
