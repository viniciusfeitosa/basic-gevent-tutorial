import gevent
from gevent.queue import Queue

tasks = Queue()


def worker(n):
    while not  # ???:
    # get from the queue
        print('Worker %s got task %s' % (n, task))
        gevent.sleep(0)

    print('%s salindo de la cola!' % (n))


def boss():
    for i in range(1, 26):
        # put the number in the queue


gevent.spawn(boss).join()

gevent.joinall([
    gevent.spawn(worker, 'Luke'),
    gevent.spawn(worker, 'Ham'),
    gevent.spawn(worker, 'Lea'),
])
