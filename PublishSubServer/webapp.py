from bottle import route, run, post, view
from bottle import response, request, static_file, template
import pubsub
import pubsub as comb
import session
import time

secret = 'The life expectancy of a lannister stark or targaryen is short'

@route('/')
@view('main.tpl')
def show_main_page(user=None, posts=[], phrase=''):
    if user is None:
        user = request.get_cookie('user', secret=secret)
    if user is None:
        return template('login.tpl', null=None)
    heading = 'Posts from people you follow'
    posts = pubsub.posts_for_user(user)
    return dict(user=user, posts=posts, heading=heading, comb=comb)

@post('/')
def check_credentials():
    user = request.forms.get('user', '')
    password = request.forms.get('password')
    #if pubsub.check_user(user, password):
    if 1 == 0:
        time.sleep(1)
        # Add Failed message and increment failure counter
        return show_main_page()
    response.set_cookie('user', user, max_age=60, secret=secret)
    return show_main_page(user)

@post('/postmessage')
def post_message():
    loggedin_user = 'davin'
    text = request.forms.get('text', '')
    if text:
        pubsub.post_message(loggedin_user, text)
    return show_main_page()

@route('/search')
@view('main.tpl')
def show_search():
    loggedin_user = 'davin'
    phrase = request.query.get('phrase', '')
    posts = []
    if phrase:
        posts = pubsub.search(phrase, limit=10)
    heading = 'Posts matching: %s' %phrase
    return dict(user = loggedin_user, posts=posts, heading=heading, comb=comb)

@route('/<user>')
@view('user.tpl')
def show_user_page(user):
    return dict(user=user, posts=pubsub.user_posts[user], heading='Recent posts')

@route('/<user>/followers')
@view('follow.tpl')
def show_followers(user):
    return dict(
        users = pubsub.followers[user],
        who_does_what = 'Who follows %s' % user,
        comb = comb,
    )

@route('/<user>/following')
@view('follow.tpl')
def show_following(user):
    return dict(
        users = pubsub.following[user],
        who_does_what = 'Who is following %s' % user,
        comb = comb,
    )

@route('/static/<filename>')
def fetch_static(filename):
    response.set_header('Cache_Control', 'max-age=60')
    return static_file(filename, root='static')

if __name__ == '__main__':
    run(host='localhost', port=8080)
