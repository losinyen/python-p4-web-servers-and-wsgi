# server/werkzeug_app.py

from werkzeug.wrappers import Request, Response # type: ignore
from werkzeug.serving import run_simple # type: ignore

@Request.application
def application(request):
    print(f'This web server is running at {request.remote_addr}')
    return Response('A WSGI generated this response!')

if __name__ == '__main__':
    run_simple('localhost', 5555, application)
