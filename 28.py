limit = int(input("Upper limit:"))
words = "1"
number = 1
while number != limit:
    number += 1
    words += f" + {number}"
print(f"{words} = {limit}")