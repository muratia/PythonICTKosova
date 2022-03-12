from datetime import date, time, datetime
# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    doit()
    yield n

    n += 1
    print('This is printed at last')
    yield n

    n += 2
    print('This is printed after the last')
    yield n


def doit():
    print('This is printed second')
    print(date.today())
    current_time = datetime.today().strftime("%H:%M:%S")
    print(current_time)


a = my_gen()

next(a);
next(a);
next(a);
next(a);