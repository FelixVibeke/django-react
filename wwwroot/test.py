def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [bytes("<html><body><h1 style='color:blue'>Hello There!</h1></body></html>",'utf-8')]