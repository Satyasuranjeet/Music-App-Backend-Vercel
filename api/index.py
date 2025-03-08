from app import app

def handler(event, context):
    from werkzeug.wrappers import Request, Response
    try:
        request = Request(event)
        response = Response()
        return app(request.environ, response.start_response)
    except Exception as e:
        return {
            "statusCode": 500,
            "body": f"Internal server error: {str(e)}"
        }