import requests

def fetchandSaveToFile(url, path):
    r=requests.get(url)
    with open(path, "w") as f:
        f.write(r.text) 
        
url= "https://timesofindia.indiatimes.com/city/delhi"

fetchandSaveToFile(url, "data/timesofindia.html")