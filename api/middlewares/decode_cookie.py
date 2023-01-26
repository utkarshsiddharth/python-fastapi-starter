from fastapi import Request

def decode_cookie_middleware(request:Request, call_next ):
    cookies = request.cookies
    token = cookies.get('auth_token')
    if token:
        print(token)
    response = call_next(request)
    return response

class DecodeCookieMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        assert scope["type"] == "http"
        request = Request(scope, receive)
        cookies = request.cookies
        token = cookies.get('auth_token')
        headers = dict(scope["headers"])
        headers[b"Authorization"] = bytes(f"Bearer {token}", 'utf-8') # generate the way you want
        scope["headers"] = [(k, v) for k, v in headers.items()]
        await self.app(scope, receive, send)