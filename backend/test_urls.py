import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

url = "https://portal-psc.ap.gov.in/HomePages/RecruitmentNotifications"

response = requests.get(
    url,
    headers=HEADERS,
    timeout=20
)

print("Status:", response.status_code)

with open("recruitment.html", "w", encoding="utf-8") as f:
    f.write(response.text)

print("HTML saved as recruitment.html")