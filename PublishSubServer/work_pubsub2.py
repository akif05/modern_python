'Simple  message publisher/subscriber service'
from typing import NamedTuple, DefaultDict
from collections import namedtuple, deque, defaultdict
import time

User = str
Post = NamedTuple('Post', [('timestamp', float), ('user',str), ('text', str)])

## Use list to grow right and deque to grouw left!
posts = deque()    # type: deque    #Posts from newest to oldest
user_posts = defaultdict(deque)     # type: DefaultDict[User, deque]

# The function reseives str, str, float-or None -> and returns None or C stile void
def post_message(user: User, text: str, timestamp: float=None) -> None:
    timestamp = timestamp or time.time()
    post = Post(timestamp, user, text)
    posts.appendleft(post)
    user_posts[user].appendleft(post)

