import pandas
import requests

url = "http://pages.iu.edu/~jsaxberg/data.csv"

def get_data():
    req = requests.get(url, allow_redirects=True)
    open("data/data.csv", 'wb').write(req.content)
    data = pandas.read_csv("data/data.csv")
    return(data)

def run(hlt, mil, edu, tax, wmr, glb, gnr, inf, mnr, img):
    data = get_data()
    return("Analysis finished: %s %s %s %s %s %s %s %s %s %s" % (hlt, mil, edu, tax, wmr, glb, gnr, inf, mnr, img))

