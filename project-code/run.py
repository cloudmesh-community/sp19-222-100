import os
import pandas
import requests
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix

url = "http://pages.iu.edu/~jsaxberg/pres.csv"

def get_data():
    req = requests.get(url, allow_redirects=True)
    open("data/data.csv", 'wb').write(req.content)
    data = pandas.read_csv("data/pres.csv")
    return(data)

def run_custom(neighbors, hlt, mil, edu, tax, wmr, glb, gnr, inf, mnr, img):
    data = get_data()

    x = data.iloc[:, 5:15].values
    y = data.iloc[:, -1].values

    classifier = KNeighborsClassifier(n_neighbors=int(neighbors))
    classifier.fit(x, y)

    y_pred = classifier.predict([[hlt, mil, edu, tax, wmr, glb, gnr, inf, mnr, img]])
    
    return("Your candidate with data: %s %s %s %s %s %s %s %s %s %s would %s a hypothetical presidential election according to this algorithm." % (hlt, mil, edu, tax, wmr, glb, gnr, inf, mnr, img, "WIN" if y_pred==[1] else "LOSE"))

def run_test():
    data = get_data()

    x = data.iloc[:, 5:15].values
    y = data.iloc[:, -1].values
    
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

    classifier = KNeighborsClassifier(n_neighbors=find_best(False, x_train, x_test, y_train, y_test))
    classifier.fit(x_train, y_train)

    y_pred = classifier.predict(x_test)

    matrix = str(confusion_matrix(y_test, y_pred))
    report = str(classification_report(y_test, y_pred))

    return("Confusion Matrix: %s Classification Report: %s" % (matrix, report))

def neighbors():
    data = get_data()

    x = data.iloc[:, 5:15].values
    y = data.iloc[:, -1].values

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

    best_num = find_best(True, x_train, x_test, y_train, y_test)

    return("The best n_neighbors argument to use is: %s" % str(best_num))

def find_best(graph, x_train, x_test, y_train, y_test):
    error = []

    for i in range(1, 26):
        knn = KNeighborsClassifier(n_neighbors=i)
        knn.fit(x_train, y_train)
        i_pred = knn.predict(x_test)
        error.append(np.mean(i_pred != y_test))

    if(graph == True):
        plt.plot(error)
        plt.xlabel('n_neighbors count')
        plt.ylabel('error rate')
        plt.title('Error Rate for all n_neighbor Permutations')

        if(os.path.isfile('data/imgs/neighbors.png')):
            os.remove('data/imgs/neighbors.png')

        plt.savefig('data/imgs/neighbors.png')
        
        plt.close()

        return(str(error.index(min(error)) + 1) + ". Graph can be found at endpoint /data/show/graph")
    else:
        return(str(error.index(min(error)) + 1))
