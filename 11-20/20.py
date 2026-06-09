password = input("Type in a password:\n")
while True:
    passcheck = input("Repeat password:\n")
    if password == passcheck:
        print ("Account created!")
        break
    else:
        print ("They do not match!")
