# Packing & Unpacking
def show(a, b, c):
    print(a, b, c)

nums = [10, 20, 30]
show(*nums)  # list unpacking

person = {"a": 1, "b": 2, "c": 3}
show(**person)  # dict unpacking
