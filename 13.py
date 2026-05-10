while True:
    number = int(input("Type a number:\n"))
    if number < 1000:
        print ("This number is smaller than 1000")
        if number < 100:
            print (f"{number} is smaller than 100")
            if number < 10:
                print ("This number is smaller than 10")
            else:
                print("But the number is digger than 10")
        else:
            print("But the number is higher than 100")
    else:
        print("This is more than 1000")
    print ("Thank YOOSSou!!!")