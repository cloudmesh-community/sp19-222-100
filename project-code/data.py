import requests

url = "http://pages.iu.edu/~jsaxberg/pres.csv"

def download_data(url, filename):
    req = requests.get(url, allow_redirects=True)
    open(filename, 'wb').write(req.content)

def download(output):
    fout = "data/"+output
    download_data(url=url, filename=fout)
    return("Data downloaded to " + fout + ".")

def graph():
    with open("data/imgs/neighbors.png", "rb") as image:
        f = image.read()
        b = bytearray(f)
        return(b[0])
