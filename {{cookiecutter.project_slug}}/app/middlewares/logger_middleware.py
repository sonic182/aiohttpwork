"""Logger middleware.

Adds logger adapter instance to request.
"""


async def logger_middleware(app, handler):
    """Add uuid to request."""
    async def middleware_handler(request):
        """Handle middleware behaivor."""
        request.logger = app.logger
        return await handler(request)
    return middleware_handler
