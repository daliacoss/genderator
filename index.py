import sys

def application(environ, start_response):
    output = 'Welcome to your mod_wsgi website! It uses:\n\nPython %s' % sys.version

    response_headers = [
        ('Content-Length', str(len(output))),
        ('Content-Type', 'text/plain'),
    ]

    start_response('200 OK', response_headers)

    return [output]
