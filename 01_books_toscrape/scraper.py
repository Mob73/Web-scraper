"""Objectif : Extraire le titre, le prix, la disponibilité et la note de tous les livres sur books.toscrape.com.
Outils : Python + requests + beautifulsoup4.
Livrable : Un fichier livres.csv propre contenant l'ensemble des données extraites."""
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

HEADERS = {"User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
 "AppleWebKit/537.36 (KHTML, like Gecko) "
 "Chrome/140.0.0.0 Safari/537.36"),
     "Accept-Language": "fr-FR,fr;q=0.9"}

session = requests.Session()
session.headers.update(HEADERS)

def telecharger(session, url):
    """Télécharge une page. Renvoie le texte HTML, sinon None."""
    try:
        r = session.get(url, timeout=(5, 15))
        r.encoding = 'utf-8'
        r.raise_for_status()
        return r.text
    except requests.exceptions.Timeout:
        print(f"[TIMEOUT] {url}")
    except requests.exceptions.HTTPError as e:
        print(f"[HTTP] {e.response.status_code} sur {url}")
    except requests.exceptions.RequestException as e:
        print(f"[RESEAU] {type(e).__name__} sur {url}")
        return None

html = telecharger(session, "https://books.toscrape.com/")
soup = BeautifulSoup(html, "lxml")

books = soup.find_all("article", class_="product_pod")
book_list = []
for i in range(1, 51):
    html = telecharger(session, f"https://books.toscrape.com/catalogue/page-{i}.html")
    soup = BeautifulSoup(html, "lxml")
    books = soup.find_all("article", class_="product_pod")

    for book in books:
        titre = book.find("h3").get_text()
        prix = book.find("p", class_="price_color").get_text()
        dispo = book.find("p", class_="instock availability").get_text()
        star_tag = book.find(class_="star-rating")
        star = star_tag["class"][1]
        book = {
            "titre":titre,
            "prix":prix,
            "dispo":dispo,
            "star":star
        }
        book_list.append(book)

df = pd.DataFrame(book_list)
df.to_excel("books.xlsx", index=False)