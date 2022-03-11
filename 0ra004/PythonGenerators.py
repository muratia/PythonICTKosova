# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n

    n += 2
    print('This is printed at after the last')
    yield n


a = my_gen()

next(a)
next(a)
next(a)
next(a)