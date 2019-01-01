'Simple  message publisher/subscriber service'
from typing import NamedTuple
from collections import namedtuple, deque, defaultdict
import time

Post = namedtuple('Post', ['timestamp', 'user', 'text'])

## Use list to grow right and deque to grouw left!
posts = deque()    # Posts from newest to oldest
user_posts = defaultdict(deque)

def post_message(user, text, timestamp=None):
    timestamp = timestamp or time.time()
    post = Post(timestamp, user, text)
    posts.appendleft(post)
    user_posts[user].appendleft(post)

