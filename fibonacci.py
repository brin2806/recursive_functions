'''two key elements of a recursive function are:
1. The termination condition
2. The reduction step, where the function calls itself with a
smaller number each time

'''
def fib(n):

    if n <= 1:
        return n
    else:
        return (fib(n-1) + fib(n-2))

print fib(15)

def fib_lst(n):
    lst = []
    for num in range(n+1):
        lst.append(fib(num))
    return lst

print fib_lst(15)


def fib_even(n):
    lst = [] # create an empty list
    for num in range(n+1):
        if fib(num) % 2 == 0: # ascertain if its even
            lst.append(fib(num)) #append item to teh list
    return lst

print fib_even(15)

def isEven(num):
    return num % 2 == 0

def fibonacci(n):
    if n <= 1:
        return n

    else:
        return (fibonacci(n-1) + fibonacci(n-2))

'''using map and filter:
mapping: is a method of transforming one tuple into another by applying a function to each elemnt and collecting
the results.
eg:
alternates = (-1,2,-3,4,-5)
tuple(map(abs, alternates))
(1,2,3,4,5). # the map allows us to access each eleemnt in the tuple and pas it as
an argument into the mapped function ie abs.

filter function: takes a sequence and returns those elements of sequence for which
the predicate is true.
eg:
nums = (5,6, -7, -8, -9)
tuple(filter(iseven, nums))
(6, -8)
'''

# getting a list of even numbers within 20

print filter(isEven, map(fibonacci, range(20)))


