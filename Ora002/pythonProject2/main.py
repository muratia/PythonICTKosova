# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    vargu = [
        "Tregu", "Qendra", "Qendra"
    ]
    bashkesia = {"Tregu", "Qendra", "Qendra"}

    print(vargu)
    print(bashkesia)

def readAFile():
    # Open a file
    fo = open("foo.txt", "r+")
    print ("Name of the file: ", fo.name)

    line = fo.read(10)
    print ("Read Line: %s" % (line))

    # Close opened file
    fo.close()

def writeToFile():
    # Open a file
    fo = open("foo2.txt", "w")
    fo.write("Python is a great language.\nYeah its great!!\n")

    # Close opend file
    fo.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    readAFile()
    writeToFile()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
