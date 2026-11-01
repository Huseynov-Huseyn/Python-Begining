# keyword argument =an argument preceded by identifier and helps with readability
#   order of arguments doesn't matter
# positional argument = values are matched to parameters by their order
def greeting(title, name, surname):
    print(f"Hello {title} {name} {surname}")


# positional arguments must come before keyword arguments:
# greeting(name="Huseyn", "Mr.", "Huseynov")   <- SyntaxError
greeting("Mr.", "Huseyn", "Huseynov")
greeting("Mr.", name="Huseyn", surname="Huseynov")
greeting("Mr.", surname="Huseynov", name="Huseyn")

#  sep and end are keyword arguments of print
for i in range(4):
    print(i, end=" ")
print()
print("1", "2", "3", "4", sep="-")


def number(country, area, first, mid, last):
    print(f"+{country}-{area}-{first}-{mid}-{last}")


number("994", "50", "000", last="00", mid="00")
