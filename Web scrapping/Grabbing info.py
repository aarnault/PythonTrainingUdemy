import requests
import bs4

result = requests.get("https://example.com/")

soup = bs4.BeautifulSoup(result.text, "lxml")

soup.select("title")[0].getText()
site_paragraphs = soup.select("p")
site_paragraphs[0].getText()

res = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')
soup = bs4.BeautifulSoup(res.text, "lxml")

first_item = soup.select('.toctext')[0]
first_time.text

for item in soup.select('.tocext'):
    print(item.text)


res = requests.get ('https://en.wikipedia.org/wiki/Deep_Blue_%28chess_computer%29')
soup = bs4.BeautifulSoup(res.text, "lxml")

soup.select('.thumbimage')

computer = soup.select('.thumbimage') [0]
computer['src']
<img src='//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/220px-Deep_Blue.jpg'>

image_img = requests.get('//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/220px-Deep_Blue.jpg')

f = open('my_computer_image.jpg', 'wb')
f.write(image_link.content)

f.close()

