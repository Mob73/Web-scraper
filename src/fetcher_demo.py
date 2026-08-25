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
annonces = soup.find_all(class_ = "card")
print(annonces[0].get_text())



"""with open('coinafrique.txt', 'a') as f:
    for prod, price in zip(products[:10], prices[:10]):
        f.write(f"Produit : {prod} | Prix : {price}\n")
"""
"""for img_url in soup.find_all("img", class_ = "ad__card-img",src=True):
    url = img_url["src"]
    images.append(url)
images = images[:10]
for i in range(len(images)):
    response = session.get((images[i]))
    with open(f"image{i}.jpg", "wb") as f:
        f.write(response.content)
    print("téléchargement éffectué")"""