import requests
import bs4


result = requests.get("http://quotes.toscrape.com/")
#result.text

soup = bs4.BeautifulSoup(result.text, "lxml")

soup.select('.author') # as it is a class so .
authors =[]
for n in soup.select('.author'):
    authors.add(n.text)

#authors
quotes = []
for quote in soup.select('.text'):
    quotes.append(quote.text)

#quotes

for item in soup.select('.tag-item'):
    print(item.text)


url ='http://quotes.toscrape.com/page/'

url+str(10)

authors = set()
for page in range(1, 10):
    page_url =url +str(page)
    result = requests.get(page_url)
    soup = bs4.BeautifulSoup(res.text, "lxml")

for n in soup.select('.author'):
    authors.add(n.text)
#authors

page_url+str(99999)
res = requests.get(page_url)

soup=bs4.BeautifulSoup(res.text, 'lxml')

"No quotes found!" in res.text

page_still_valid = True
authors = []
page =1
while page_still_valid:
    page_url = url+str(page)
    result = requests.get(page_url)
    if "No quotes found!" in result.text:
        break
    soup = bs4.BeautifulSoup(res.text, "lxml")
    for n in soup.select('.author'):
        authors.add(n.text)

    page = page+1

