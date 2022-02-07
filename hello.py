def one(environ, start_response):
    status = '200 OK'
    responce_headers = [('Content-type', 'text/plain')]
    start_response(status, responce_headers)
    session = environ['QUERY_STRING']
    result = ''
    for n in session:
       	if n == '&':
            result += '\n'
        else:
            result += n
    return [bytes(str(result), encoding='utf-8')]
