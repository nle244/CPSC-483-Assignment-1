import csv
from turtle import clear
from unittest import result
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier, NearestNeighbors

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
my_predict = []
num_neighbors = 5

#Building training and test set
with open('happiness_last.csv', newline= '') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        if(count > 0 and count < 113):
            row = [eval(x) for x in row]
            training.append(row)
        if(count >= 113):
            row = [eval(x) for x in row]
            testing.append(row)
        count = count + 1


#sorting function
def Sort_tuple(tup):
    tup.sort(key = lambda x: x[1])
    return tup

#predictions
def My_predict(training, testing):
    result =[]
    for test in testing:
        neighbors = []
        # print('test: ',test)
        for train in training:
            dist = 0
            # print('train: ',train)
            for i in range(len(test[:-1])):
                dist = dist + abs(test[i] - train[i])
            neighbors.append((train[-1], dist))
        Sort_tuple(neighbors)

        #find the closest neighbors
        value = 0
        for i in range(num_neighbors):
            # print(neighbors[i][0])
            value = value + float(neighbors[i][0])
        
        #calculate the prediction
        prediction_value = round(value/num_neighbors,0)
        result.append(int(prediction_value))
    return result

print('My predictions: ',My_predict(training, testing))

#scikit KNN
def SK_predict(training, testing):
    sk_predict = []
    x_train = []
    y_train = []
    x_test = []
    y_test =[]
    for row in training:
        x_train.append(row[:5])
        y_train.append(row[-1])
    for row in testing:
        x_test.append(row[:5])
        y_test.append(row[-1])

    neigh = KNeighborsClassifier(n_neighbors=num_neighbors)
    # neigh.fit(x,y)
    neigh.fit(x_train,y_train)
    for each in x_test:
        sk_predict.append(int(neigh.predict([each])[0]))
    return sk_predict

print('Scikit predictions',SK_predict(training, testing))

#built true values
true_predict = []
for row in testing:
    true_predict.append(int(row[-1]))

print('True values: ',true_predict)

def Predict_correct(predicted,true):
    result = 0
    for i in range(len(predicted)):
        if predicted[i] == true[i]:
            result = result + 1
    result = round(result / len(predicted),2)
    return result




