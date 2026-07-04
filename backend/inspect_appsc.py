import requests
from bs4 import BeautifulSoup

url = "https://portal-psc.ap.gov.in/HomePages/RecruitmentNotifications"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

print("Status Code:", response.status_code)
print("Final URL :", response.url)

print("\nResponse Length:", len(response.text))

print("\nFirst 1000 Characters\n")
print(response.text[:1000])

print("\nTitle")

soup = BeautifulSoup(response.text, "html.parser")

print(soup.title)

print("\nForms Found:", len(soup.find_all("form")))

print("Scripts Found:", len(soup.find_all("script")))

print("Tables Found:", len(soup.find_all("table")))

print("Iframes Found:", len(soup.find_all("iframe")))