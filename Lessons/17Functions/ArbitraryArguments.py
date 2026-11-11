# *args      = allow you to pass multiple non-key arguments
# *args      = packs extra positional arguments into a tuple
# **kwargs   = allow you to pass multiple keyword arguments
# **kwargs   = packs extra keyword arguments into a dictionary
def add(*args):
    # args = tuple
    print(type(args))
    total = 0
    for arg in args:
        total += arg
    return total


print(add(1, 2, 3))


# You can use any name after *
def display_name(*names):
    for name in names:
        print(name, end=" ")


display_name("Conor", "The Notorious", "McGregor")


# **kwargs
def print_address(**kwargs):
    # kwargs = dictionary
    print(type(kwargs))
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_address(city="Baku",
              street="Haci Zeynalabdin 42/15")


def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    print(f"City: {kwargs.get('city')}")
    if "number" in kwargs:
        print(f"Street: {kwargs.get('street')} {kwargs.get('number')}")
    elif "pobox" in kwargs:
        print(f"Street: {kwargs.get('street')} {kwargs.get('pobox')}")
    else:
        print(f"Street: {kwargs.get('street')}")


shipping_label("Dr", "Huseyn", "Huseynov",
               city="Baku",
               street="Haci Zeynalabdin 42/15",
               number="#012"
               )
shipping_label("Dr", "Ali", "Valiyev",
               city="Baku",
               street="Mikayil Mushfiq 12/15"
               )

shipping_label("Dr", "Ali", "Valiyev",
               city="Baku",
               street="Mikayil Mushfiq 12/15",
               pobox="PO Box #1221"
               )
