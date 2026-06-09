story = ""
while True:
    word = input("Type in a word:")
    if word == "end":
        break
    story += word + " "
print (story)