import csv

with open("Sales records.csv", 'r') as old_csv:
    with open("old.csv", 'w', newline='') as new_csv:
        print("Writing file...   ")
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)