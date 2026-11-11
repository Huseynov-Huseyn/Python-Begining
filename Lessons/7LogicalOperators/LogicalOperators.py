# or,and,not
age = 20
inCollege = True
isWorking = False
if age > 18 and inCollege:
    print("You are classified to join the group")
elif age == 20 or isWorking:
    print("You are classified to join the group, due to your CV")
elif not isWorking:
    print("You are not working")
