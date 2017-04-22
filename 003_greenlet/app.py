import gevent
from gevent import Greenlet

# What is necessary to YoSoyUnGreenlet() class be a Greenlet


class YoSoyUnGreenlet():

    def __init__(self, message, n):
        Greenlet.__init__(self)
        self.message = message
        self.n = n

    def _run(self):
        print(self.message)
        gevent.sleep(self.n)


yo = YoSoyUnGreenlet("Hi there!", 3)
yo.start()
yo.join()
