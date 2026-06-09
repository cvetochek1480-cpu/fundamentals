import csv #to use csv 
#all of the inputs:
liquid = input("Liquid Name:")
month = input ("Arrival Month:")
year = input ("Arrival Year:")
#opening a csv file in append mode and write in it and saving it:
with open ('laboratory.csv', mode='a') as file:
    writer = csv.writer(file)
    writer.writerow ([liquid,month,year])
print ("--- CURRENT LABORATORY INVENTORY ---") #decorations
#opening csv and reading it:
with open ('laboratory.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        if not row: #if there is an empty line skip it
            continue
        print(f">{row[0]} arrived in {row[1]} {row[2]}.")
print("-------------------------------------") #decorations