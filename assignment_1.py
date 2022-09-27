import csv

#move first column to last column
output_file = open("happiness_last", "a")

with open('HappinessData-1.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        temp = row[1:]
        temp.append(row[0])
        with open('happiness_last.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerows(temp)