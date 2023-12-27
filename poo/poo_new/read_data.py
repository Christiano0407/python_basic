## #* === Created Script ===
import csv 

#Read CSV Documents
with open("./data_poo/poo_data.csv", "r") as file:
  reader = csv.reader(file)
  for row in reader:
    print(row)