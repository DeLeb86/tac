import requests
from bs4 import BeautifulSoup

root_url = "https://max.de.wilde.web.ulb.be/camille/"
soup = BeautifulSoup(requests.get(root_url).content,"html.parser")
for link in soup.find_all("a"):
    title=link.text.strip()
    url = root_url + link.get('href')
    response=requests.get(url)
    with open(f"data/pdf/{title}","wb") as fh:
        fh.write(response.content)
    print(title)
