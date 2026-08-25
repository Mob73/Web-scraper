import requests
from pathlib import Path
from bs4 import BeautifulSoup
HEADERS = {
    "User-agent":("Brave"),
    "Accept":("text/html,application/xhtml+xml"),
    "Accept-Language":"fr-FR"
}
session = requests.Session()
session.headers.update(HEADERS)

def telecharger(session, url):
    """Télécharge une page. Renvoie le texte HTML, sinon None."""

    try:
        r = session.get(url, timeout=(5, 15))
        r.raise_for_status()
        return r.text
    except requests.exceptions.Timeout:
        print(f"[TIMEOUT] {url}")
    except requests.exceptions.HTTPError as e:
        print(f"[HTTP] {e.response.status_code} sur {url}")
    except requests.exceptions.RequestException as e:
        print(f"[RESEAU] {type(e).__name__} sur {url}")
        return None

html = telecharger(session, "https://tg.coinafrique.com/search?sort_by=price_desc")
soup = BeautifulSoup(html, "lxml")
annonces = soup.find_all(class_ ="card ad__card round small hoverable top undefined")
list_annonces = []
for a in annonces:
    element1 = a.find("p", class_="ad__card-description")
    element2 = a.find("p", class_="ad__card-price")
    element3 = a.find("img", class_="ad__card-img")
    element4 = a.find('p', class_="ad__card-location")
    if True:
        title = element1.get_text(strip=True)
        price = element2.get_text(strip=True)
        img = element3["src"]
        location=element4.get_text(strip=True)
        list_annonces.append({"title":title,
        "price":price,
        "location":location,
        "img":img})
    else:
        print("element non trouvé")
    
print(list_annonces[1])

annonce1 = list_annonces[0]
image = annonce1["img"]
reponse = session.get(image)
with open("images/img1.jpg", "wb") as f:
    f.write(reponse.content)
