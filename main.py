from bs4 import BeautifulSoup
with open('main.html', 'r') as file:
    content = file.read()
    print(content)