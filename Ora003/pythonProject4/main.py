# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from datetime import datetime


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    value = input("Please enter a string:\n")

    print(f'You entered {value} and its type is {type(value)}')

    value = input("Please enter an integer:\n")

    rez = int(value) * 2
    print(rez)

    print(f'You entered {value} and its type is {type(value)}')

    date_string = "2022-12-12 10:10:10"
    date = input("Give a date: ")
    print(datetime.fromisoformat(date_string))

    today = datetime.today()
    print("Today's date:", today)

    # dd/mm/YY
    d1 = today.strftime("%d/%m/%Y")
    print("d1 =", d1)

    # Textual month, day and year
    d2 = today.strftime("%B %d, %Y")
    print("d2 =", d2)

    # mm/dd/y
    d3 = today.strftime("%m/%d/%y")
    print("d3 =", d3)

    # Month abbreviation, day and year
    d4 = today.strftime("%b-%d-%Y")
    print("d4 =", d4)
    # Month abbreviation, day and year
    d5 = today.strftime("%b/%d/%Y")
    print("d5 =", d5)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
