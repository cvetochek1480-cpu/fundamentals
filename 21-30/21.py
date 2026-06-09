attempts = 0

while True:
    code = input("PIN: ")
    attempts += 1
    if attempts == 1 and code == "1234":
        print("Correct! It only took you one single attempt!")
        break
    elif code == "1234":
        print(f"Correct! It took you {attempts} attempts")
        break
    elif code != "1234":
        print("Wrong!")