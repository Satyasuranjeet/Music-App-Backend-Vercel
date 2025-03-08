from app import app

def handler(event, context):
    from werkzeug.wrappers import Request, Response
    request = Request(event)
    response = Response()
    return app(request.environ, response.start_response)