#Goal: get title of every book with 2 stars rating

import requests
impost bs4

base_url = 'http://books.toscrape.com/catalogue/page-{}.html'

res =requests.get(base_url.format(1))
soup = bs4.BeautifulSooup(res.text, 'lxml')

len(soup.select(".product_pod")) #to ensure 20 books per page

products = soup.select(".product_pod")

example = products[0]

# one way to find the books

'star-rating Two'  in str(example)

#more efficient way

example.select(".star-rating.Two")

#now grab the title

example.select('a') [1] ['title']

two_star_titles = []
for n in range (1, 51):
    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)

    soup = bs4.BeautifulSoup(res.text, 'lxml')
    books = soup.select(".product_pod")

    for book in books:
        if len(book.select('start-rating Two')) != 0
        # other way
        #if 'star-rating Two' in str(book)
            book_title = book.select('a') [1] ['title']
            two_star_titles.append(book_title)