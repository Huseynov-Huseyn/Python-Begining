name = input("Please enter your name: ")
if len(name) > 12:
    print("Username is no more than 12 characters")
elif not name.find(" ") == -1:
    print("Username must not contain spaces")
elif not name.isalpha():
    print("Username must not contain digits")
else:
    print(f"Hello {name}!")
