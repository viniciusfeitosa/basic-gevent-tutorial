import requests
import gevent.monkey
gevent.monkey.patch_socket()


def fetch(pid):
    response = requests.get('http://localhost:8080')
    result = response.json()
    name = result['name']
    consulted_at = result['consulted_at']

    print('Process %s: %s, %s' % (pid, name, consulted_at))
    return result


def synchronous():
    for i in range(1, 10):
        fetch(i)


def asynchronous():
    threads = []
    for i in range(1, 10):
        threads.append(gevent.spawn(fetch, i))
    gevent.joinall(threads)


print('Synchronous:')
synchronous()

print('Asynchronous:')
asynchronous()
