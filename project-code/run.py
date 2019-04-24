import pandas
import requests
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
    return("Hi!")

def neighbors():
    return("Hii!")
