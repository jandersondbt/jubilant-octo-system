from bs4 import BeautifulSoup

html = "<html><body><h1>laskjflsjflj lkjlskdjfljs f .mp3</h1></body>"
soup = BeautifulSoup(html, "html.parser")
print(soup.h1.text) # Output: Hello!
