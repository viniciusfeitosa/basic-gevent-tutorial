import gevent
from gevent.event import Event


evt = Event()


def setter():
    print('The rebelian has a problem')
    gevent.sleep(3)
    print("- Leia: Ok, I'm done, it's the message")
    evt.set()


def waiter():
    print("- R2D2: bip bip")
    evt.wait()  # blocking
    print("- Message: Obi Wan, we need your help")


def main():
    gevent.joinall([
        gevent.spawn(setter),
        gevent.spawn(waiter),
        gevent.spawn(waiter),
        gevent.spawn(waiter),
        gevent.spawn(waiter),
        gevent.spawn(waiter)
    ])


if __name__ == '__main__':
    main()
