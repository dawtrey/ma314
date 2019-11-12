import time

# Remove the sleep function and implement your recursive Fibonacci function here:
def fib_recursive(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)


# time.time() gives a floating point number which is the time in seconds
# since the start of the current "epoch" of the operating system, which
# is usually the start of 1970, but not taking into account leap seconds.
start1 = time.time()
fib_recursive(34)
end1 = time.time()

elapsed1 = end1 - start1
print(elapsed1)

start2 = time.time()
fib_recursive(35)
end2 = time.time()

elapsed2 = end2 - start2
print(elapsed2)

print(elapsed2/elapsed1)

