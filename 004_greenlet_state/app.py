import gevent


def jedi_msg():
    return 'May the force be with you'


def sith_msg():
    raise Exception('Luke, I\'m your father')


jedi = gevent.spawn(jedi_msg)
sith = gevent.spawn(sith_msg)

# print if the workers have started

try:
    gevent.joinall([jedi, sith])
except Exception as e:
    print('This will never be reached')

# print the workers values

# print if the workers have finished

# print workers successful message

# print the sith execption
