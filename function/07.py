#Problem: Write a function that takes variable number of arguments and returns their sum.__


def sum_all(*args):
    return sum(args)

print(sum_all(1,2,3,7,9))

############################

def sum_all(*args):
    print(args)
    for i in args:
        print(i*2)
    return sum(args)

print(sum_all(1,2,3))

