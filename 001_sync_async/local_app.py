import gevent
import time


def task(pid):
    """
    Some non-deterministic task
    """
    time.sleep(1)
    print('Task %s done' % pid)


def synchronous():
    for i in range(1, 10):
        task(i)


# Create the asynchronous function


print('Synchronous:')
synchronous()

print('Asynchronous:')
asynchronous()
