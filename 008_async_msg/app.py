import gevent
from gevent.event import AsyncResult
a = AsyncResult()


def setter():
    print('...')
    gevent.sleep(3)
    # set the message "I'm a Jedi!"


def waiter():
    # print the message sent by the setter() function
    print('Oh...')


gevent.joinall([
    gevent.spawn(setter),
    gevent.spawn(waiter),
])
