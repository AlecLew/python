from bottle import route, run

@route('/hello')
def  hello():
    return 'Hello this is a test'

run(host='localhost', port=8080, debug=True)
