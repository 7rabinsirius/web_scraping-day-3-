from bs4 import BeautifulSoup
import requests

link = "https://www.bbc.com/"

source = requests.get(link).text

soup = BeautifulSoup(source, "html5lib")
titles = soup.find_all("h2", attrs={"data-testid": "card-headline"})

"""for title in titles:
    print(title.text)"""

with open("news.txt", "w") as file:
    for title in titles:
        file.write(title.get_text(strip=True) + "\n")
