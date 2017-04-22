import gevent
import signal


def run_forever():
    gevent.sleep(1000)


if __name__ == '__main__':
    # How we can kill a gevent zombie process?
    thread = gevent.spawn(run_forever)
    thread.join()
