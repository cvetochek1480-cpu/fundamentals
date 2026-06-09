def line(a, b):
    print(b*a)
    if b == "":
        print(a*"*")
a = int(input("Number:"))
b = input("Character:")
line(a,b)