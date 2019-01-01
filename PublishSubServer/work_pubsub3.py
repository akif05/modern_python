'Simple  message publisher/subscriber service'
from typing import NamedTuple, DefaultDict
from collections import namedtuple, deque, defaultdict
import time

User = str
Timestamp = float
Post = NamedTuple('Post', [('timestamp', float), ('user',str), ('text', str)])

## Use list to grow right and deque to grouw left!
posts = deque()    # type: deque    #Posts from newest to oldest
user_posts = defaultdict(deque)     # type: DefaultDict[User, deque]
following = defaultdict(set)                  # type: DefaultDict[User, Set[User]]
followers = defaultdict(set)                  # type: DefaultDict[User, Set[User]]

# The function reseives str, str, float-or None -> and returns None or C stile void
def post_message(user: User, text: str, timestamp: Timestamp=None) -> None:
    timestamp = timestamp or time.time()
    post = Post(timestamp, user, text)
    posts.appendleft(post)
    user_posts[user].appendleft(post)

def follow(user: User, followed_user: User) -> None:
    following[user].add(followed_user)
    followers[followed_user].add(user)
