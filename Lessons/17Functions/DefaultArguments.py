# default arguments= A default value for certain parameters
import time


def net_price(list_price, discount=0, tax=0.14):
    return list_price * (1 - discount) * (1 + tax)


print(net_price(600))
print(net_price(600, 0.1))
print(net_price(600, 0.1, 0))


def timer(end, start=0):
    for second in range(start, end + 1):
        print(second)
        time.sleep(1)


# default parameters must come last in the definition, otherwise SyntaxError:
# def timer(start=0, end):   <- SyntaxError

timer(10, 4)
