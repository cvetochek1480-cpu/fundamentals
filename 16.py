while True:
    print("Let's solve your quadratic equation!\n")
    a = float(input("Your a is:\n"))
    b = float(input("Your b is:\n"))
    c = float(input("Your c is:\n"))
    D = b**2-4*a*c
    from math import sqrt
    x1 = (-b + sqrt(D))/2*a
    x2 = (-b - sqrt(D))/2*a
    print (f"Your roots are: {x1} {x2}")
    m = input("Do you have another quadratic equation?(y/n)\n") #m refers to "more"
    if m == "n":
        break