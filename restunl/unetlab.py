from .server import RestServer


REST_SCHEMA = {
    'login': 'auth/login',
    'logout': 'auth/logout',
    'status': '/status',
    'list_templates': '/list/templates/'
}

class UnlServer(RestServer):

    def __init__(self, address):
        super(UnlServer, self).__init__(address)

    def login(self, user, pwd):
        api_call = REST_SCHEMA['login']
        payload = {
            'username': user,
            'password': pwd
        }
        resp = self.add_object(api_call, data=payload)
        self.set_cookies(resp.cookies)
        return resp

    def logout(self):
        api_call = REST_SCHEMA['logout']
        resp = self.get_object(api_call)
        return resp

    def get_status(self):
        api_call = REST_SCHEMA['status']
        resp = self.get_object(api_call)
        return resp

    def get_templates(self):
        api_call = REST_SCHEMA['list_templates']
        resp = self.get_object(api_call)
        return resp

