from bs4 import BeautifulSoup
with open('main.html', 'r') as file:
    content = file.read()
    # print(content)
    soup = BeautifulSoup(content, 'lxml')
    tags = soup.find_all('ul')
    print(tags)
    for fruits in tags:
        print(fruits.text)
    # print(soup.prettify())