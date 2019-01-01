'Sample data to test the pubsub internals'

from pubsub import *
from pprint import pprint
from itertools import islice
from heapq import merge

post_message('guido', 'i love #python type hinting')
post_message('raymandh', '#python tip: use named tuples')
post_message('guido', 'join a band today')
post_message('raymandh', '#python tip: Develop interactively')
post_message('barry', 'learn emacs')
post_message('raymandh', '#python tip: Have fun progarming')
post_message('davin', 'Teaching python today')
post_message('barry', 'emacs rocks')
post_message('raymandh', '#python tip: Never mutate while itarating')

follow('guido', followed_user='raymandh')
follow('guido', followed_user='barry')
if __name__ == '__main__':

    # assert check_user('raymandh', password='superman123')
    # assert not check_user('davin', password='passw0rd')

    #pprint(posts)

    # Print the post from particular user
    #pprint(user_postss['raymandh'])
    
    #pprint(following)
    #pprint(followers)



    #print(user_posts['raymandh'])
    #print(len(user_posts['raymandh']))
    #print(list(user_posts['raymandh']))
    # print only frist two element from the list
    #print(list(user_posts['raymandh'])[:2])


    # We can use islice to iterate
    # Get first two posts
    # If passed None to islice will get whole list
    #print(list(islice(user_posts['raymandh'], 2)))
    #print(list(islice(user_posts['raymandh'], None)))
   
   # pprint(posts_by_user('raymandh', limit=3))


    # pprint(posts_for_user('guido', limit=3))
    

    #for post in posts:
    #    if '#python' in post.text:
    #        print(post)

    #pprint(search('#python'))
    pprint(search('emacs', 1))

    
