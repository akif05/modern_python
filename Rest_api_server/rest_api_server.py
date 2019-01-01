from bottle import *
from pprint import pprint
import time
import algebra
import os

@route('/')
def welcome():
    # Next print will print in server console the headers fro client request
    #print(dict(request.headers))

    response.set_header('Vary', 'Accept')
    # Depending of the content of the request header tack desission
    if 'text/html' in request.headers.get('Accept', '*/*'):
        response.content_type = 'text/html'
        return '<h1> Howdy! </h1>'
    response.content_type = 'text/plain'
    return 'Hello\n'

@route('/now')
def time_service():
    response.content_type = 'text/plain'
    # Set caching time. Tel the caching server for how long to cache
    response.set_header('Cache-Control', 'max-age=1')
    return time.ctime()

# http://localhost:8080/upper/happy will print HAPPY on browser
@route('/upper/<word>')
def upper_case_service(word):
    response.content_type = 'text/plain'
    return word.upper()

secret = 'the average life expectancy of a stark or targaryen is short'

@route('/area/circle')
def circle_area_service():
    last_visit = request.get_cookie('last-visit', 'unknown', secret=secret)
    print(f'Last visit {last_visit}')
    response.set_cookie('last-visit', time.ctime(), secret=secret)
    response.set_header('Vary', 'Accept')
    try:
        radius = float(request.query.get('radius', '0.0'))
    except ValueError as e:
        #return f'Error: expected a float instead of {radius!r}'
        return e.args[0] 
    area = algebra.area_circle(radius)
    if 'text/html' in request.headers.get('Accept', '*/*'):
        return f'<p> The area is <em> {area} </em> </p>'
    return dict(radius=radius, area=area, service=request.path)


## File Server ################################################
file_template = '''\
<h1> List of files in <em> Congress Data </em> directory </h1>
<hr>
<ol>
 % for file in files:
    <li> <a href="files/{{file}}"> {{file}} </a> </li> 
 %end
'''
data_dir = '/Users/akifyusein/PycharmProjects/modernpython/CSVs'
@route('/files')
def show_files():
    response.set_header('Vary', 'Accept')
    files = os.listdir(data_dir)

    # If you don't want html?
    if 'text/html' not in request.headers.get('Accept', '*/*'):
        return dict(files=files)
    return template(file_template, files=files)

@route('/files/<filename>')
def serve_one_file(filename):
    return static_file(filename, data_dir) 

if __name__ == '__main__':
    run(host = 'localhost', port = 8080)
