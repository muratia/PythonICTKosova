print("Variable scope")

x = "global"
c = 2
print(f"C = {c}")


def foo():
    print("x inside:", x)
    global c
    c = 3
    print(f"C = {c}")


foo()
print("x outside:", x)
print(f"C = {c}")
