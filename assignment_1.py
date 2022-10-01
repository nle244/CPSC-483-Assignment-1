import csv
from turtle import clear
from unittest import result
import pandas as pd


#finding mean values
df = pd.read_csv('HappinessData-1.csv')

#replace missing values with the mean value
list = df.fillna(df.mean()).values.tolist()

#move first column to the last column
result = []
for row in list:
    temp = []
    temp = row[1:]
    temp.append(row[0])
    result.append(temp)

with open('happiness_last.csv', 'w', newline= '') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['City Services Availability','Housing Cost','Quality of schools','Community trust in local police','Community Maintenance','Availability of Community Room ','Unhappy/Happy'])
    writer.writerows(result)

#Use Pearson Correlation
print(df.corr(method='pearson')) #City Services Avalibility seems to have the highest correlation value

#KNN
count = 0
training = []
testing = []
prediction = []

#Building training and test set
with open('happiness_last.csv', newline= '') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        if(count > 0 and count < 113):
            training.append(row)
        if(count >= 113):
            testing.append(row)
        count = count + 1

#predictions
# neighbors = []
# for test in testing:
#     dist = 0
#     for train in training:
#         for x in test[:-1]:
#             dist = 




