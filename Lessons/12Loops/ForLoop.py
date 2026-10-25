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
