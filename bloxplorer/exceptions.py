class BloxplorerException(Exception):

    def __init__(self, message, resource_url, request_method):
        self.message = message
        self.resource_url = resource_url
        self.request_method = request_method

    def __str__(self):
        return f'{self.message} (URL: {self.resource_url}, Method: {self.request_method})'


class BlockstreamClientError(BloxplorerException):
    pass


class BlockstreamClientTimeout(BloxplorerException):
    pass


class BlockstreamClientNetworkError(BloxplorerException):
    pass


class BlockstreamApiError(BloxplorerException):
    def __init__(self, message, resource_url, request_method, status_code):
        super().__init__(message, resource_url, request_method)
        self.status_code = status_code

    def __str__(self):
        return f'{self.message} ' \
            f'(URL: {self.resource_url}, Method: {self.request_method}, ' \
            f'Status code: {self.status_code})'
