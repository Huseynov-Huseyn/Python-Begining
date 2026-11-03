# Scope = where a variable is visible and accessible
# LEGB (lookup order): Local -> Enclosing -> Global -> Built-in
# Local     = names defined inside a function (loops and if blocks do NOT create a scope)
# Enclosing = names of the outer function, seen by a nested function
# Global    = names at the top level of the file, including imported names (pi)
# Built-in  = names Python provides: print, len, range, int ...
from math import pi

print(pi)


def func1():
    # Local Scope and a is local variable
    a = 1
    print(a)


def func2():
    b = 2
    print(b)


func1()
func2()


def func3():
    c = 2
    print(c)

    def func4():
        d = 4
        print(d)

    func4()


func3()


def func5():
    # z = 5
    print(z)


z = 10
func5()

# in python, you only have function scope, which means you cannot get a variable
# which located inside the function
for i in range(3):
    x = i * 2
print(i, x)

# Assignment inside a function creates a new local variable. This is the most common error:
count = 0


def increase():
    count = count + 1  # UnboundLocalError


increase()
