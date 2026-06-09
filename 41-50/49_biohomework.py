import csv
liquid = input("Liquid Name:")
month = input ("Arrival Month:")
year = input ("Arrival Year:")
with open ('laboratory.csv', mode='a') as file:
    writer = csv.writer(file)
    writer.writerow ([liquid,month,year])
print ("--- CURRENT LABORATORY INVENTORY ---")
with open ('laboratory.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        if not row:
            continue
        print(f">{row[0]} arrived in {row[1]} {row[2]}.")
print("-------------------------------------")