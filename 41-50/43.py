def print_many_times(text, times):
    for i in range (times):
        print (text)
text = input("Type in a string:")
times = int(input("Times to print:"))
print_many_times(text, times)