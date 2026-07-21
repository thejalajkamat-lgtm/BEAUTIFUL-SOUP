from bs4 import BeautifulSoup
with open('main.html', 'r') as file:
    content = file.read()
    # print(content)
    soup = BeautifulSoup(content, 'lxml')
    tags = soup.find_all('body')
    print(tags)
    for fruits in tags:
        juice = fruits.h5.text
        print(juice)
    print(soup.prettify())