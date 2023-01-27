

class CountRequestsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.count_requests = 0
        self.count_exceptions = 0

    def __call__(self, request, *args, **kwargs):
        self.count_requests += 1
        request.request_counter = self.count_requests
        #logger.info(f"Handled {self.count_requests} requests so far")
        return self.get_response(request)
    
    def get_request_count(self):
        return self.count_requests

    def reset_count(self):
        self.count_requests = -1
        #request.request_conter = 0
