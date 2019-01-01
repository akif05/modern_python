'Simple  message publisher/subscriber service'
from typing import NamedTuple, DefaultDict, Optional, List, Set
from collections import namedtuple, deque, defaultdict
from itertools import islice
from heapq import merge
import time
from sys import intern

User = str
Timestamp = float
Post = NamedTuple('Post', [('timestamp', float), ('user',str), ('text', str)])

## Use list to grow right and deque to grouw left!
posts = deque()                     # type: deque    #Posts from newest to oldest
user_posts = defaultdict(deque)     # type: DefaultDict[User, deque]
following = defaultdict(set)        # type: DefaultDict[User, Set[User]]
followers = defaultdict(set)        # type: DefaultDict[User, Set[User]]

# The function reseives str, str, float-or None -> and returns None or C stile void
def post_message(user: User, text: str, timestamp: Timestamp=None) -> None:
    user = intern(user)
    timestamp = timestamp or time.time()
    post = Post(timestamp, user, text)
    posts.appendleft(post)
    user_posts[user].appendleft(post)

def follow(user: User, followed_user: User) -> None:
    user, followed_user = intern(user), intern(followed_user)
    following[user].add(followed_user)
    followers[followed_user].add(user)

def posts_by_user(user: User, limit: Optional[int]=None) -> List[Post]:
    return list(islice(user_posts[user], limit))

def posts_for_user(user: User, limit: Optional[int]=None) -> List[Post]:
    relevant = merge(*[user_posts[followed_user]
                    for followed_user in following[user]], reverse=True)
    return list(islice(relevant, limit))
    #return list(merge(*[user_posts[fu] for followed_user in following[user]], reverse=True))
    #return [user_posts[fu] for followed_user in following[user]]

'''This says take the user and find every user that's being followed. 
For each one of the followed_users, find all of their posts. 
Merge those posts together by timestamp, but only as needed; it makes an iterator. 
Then use the limit to peel off exactly the ones that we need. 
In our test code, we can print out the posts for davin, now limited to only two, 
and it's got the newest one from raymond and the newest one for barry. '''


def search(phrase: str, limit: Optional[int]=None) -> List[Post]:
    return list(islice((post for post in posts if phrase in post.text), limit))
    #return [post for post in posts if phrase in post.text]
