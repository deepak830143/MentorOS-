from bs4 import BeautifulSoup

with open("recruitment.html", "r", encoding="utf-8") as file:
    html = file.read()

soup = BeautifulSoup(html, "html.parser")

print("=" * 100)
print("TEXT_A DIV")
print("=" * 100)

text_div = soup.find("div", class_="text_a")

if text_div:
    print(text_div.prettify())
else:
    print("text_a div not found")