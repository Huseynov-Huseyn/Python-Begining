# for loop syntaxis
# for variable in range(start,end,step):

for counter in range(1, 11):
    print(f"Count {counter}")

# IS NOT WORKING
# for x in range(11, 1):
#     print(f"{x} till new year!")
# print("Happy New Year!")

for time in reversed(range(1, 11)):
    print(f"{time} second till new year")
print("Happy New Year!")

for even in range(0, 100, 2):
    print(even)

credit_card = "1234-5678-9012-3456"
for x in credit_card:
    if x == "-":
        continue
    else:
        print(x)

# in Python the else clause is executed after the loop finishes its final iteration
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n // x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

# range() does not create a list, it returns a range object
print(range(20))
# sum() adds all numbers in range: 0 + 1 + ... + 19 = 190
print(sum(range(20)))
