name = "abubakar"

# length of String. result in integer
print(len(name))

# index of a symbol. if the symbol doesn't exist, return -1
# if the method finds the symbol, it will return it and don't go forward to find
print(name.find("u"))
print(name.rfind("u"))
print(name.capitalize())
print(name.upper())
print(name.lower())

# if String contains only digit returns true else false
print(name.isdigit())
# if String contains only alphabetical characters, returns true, else false
# space is not an alphabetical character
print(name.isalpha())

phone_number = "+994 - 55 - 999 - 99 - 99"
print(phone_number.count("-"))
print(phone_number.replace("-", ""))

# You can learn another string method with help method
print(help(str))
