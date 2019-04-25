import csv

#with open("Book1.csv", "r") as old_csv:
    #reader = csv.reader(old_csv)
    #for row in reader:
   #     old_number = row[0]
  #      writer = csv.writer (new_csv)
 #       print(int(old_number) + 1)

#        print(old_number)

with open("Book1.csv", "r") as old_csv:
    with open ("MyNewFile.csv", 'W', newline=0) as (new_csv):
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        print("Processing....")

        for row in reader:
            old_number = row[0]
            first_num = int(old_number[0])
            if first_num


