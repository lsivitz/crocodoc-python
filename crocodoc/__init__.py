import document, session, download

api_token = ""
base_url = "https://crocodoc.com/api/v2/"

class APIError(Exception):
    def __init__(self, message, response=None):
        Exception.__init__(self, message)
        self.error_message = message
        self.response_content = None
        self.status_code = None

        if response is not None:
            self.status_code = response.status_code
            self.response_content = response.content
            
    def __str__(self):
        content = self.response_content
        if self.response_content and len(self.response_content) > 100:
            content = self.response_content[:100] + "..."
        params = (self.error_message, self.status_code, content)
        return "\n\t%s \n\tResponse status code: %s \n\tResponse content: %s" % params
        
class InvalidParamError(APIError): pass