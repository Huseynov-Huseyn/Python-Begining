# Indexing = accessing symbol using []
# [start : end : step]
name = "Idare Et"
numbers = "0123456789"
print(name[2])
print(numbers[:4])
print(numbers[4:])
print(numbers[0: 10: 2])
print(numbers[::2])
print(numbers[-1])

credit_card = "1234-5678-9012-3456"
last_four = credit_card[-4:]
print(f"****-****-****-{last_four}")

# Reverse a String
reverse_credit_card = credit_card[::-1]
print(reverse_credit_card)
