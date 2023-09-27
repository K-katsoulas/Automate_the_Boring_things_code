def a():
    print('a() Starts')
    b()
    d()
    print('a() Returns')


def b():
    print('b() starts ')
    c()
    print('b() returns')


def c():
    print('c() Starts')
    print('c() returns')


def d():
    print('d() Starts')
    print('d() Returns ')


a()
