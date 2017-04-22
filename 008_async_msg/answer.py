import gevent
from gevent.event import AsyncResult
a = AsyncResult()


def setter():
    print('...')
    gevent.sleep(3)
    a.set("I'm a Jedi!")


def waiter():
    print(a.get())
    print('Oh...')


gevent.joinall([
    gevent.spawn(setter),
    gevent.spawn(waiter),
])
