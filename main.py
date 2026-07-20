import os
import requests
def fetchAndSaveToFile(url, path):
    r = requests.get(url)
    with open(path, "w") as f:
        f.write(r.text)
url = "https://economictimes.indiatimes.com/"
fetchAndSaveToFile(url, "data/times.html")
# r = requests.get(url)
# print(r.text)

# with open("demo.txt", "r") as f:
#     data = f.read()
#     print(data)