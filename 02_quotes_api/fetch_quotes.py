"""Objectif : Aller sur [quotes.toscrape.com/scroll](https://quotes.toscrape.com/scroll), ouvrir les outils de développement de votre navigateur (Touche F12 > onglet Réseau/Network > filtre Fetch/XHR), repérer l'endpoint API qui renvoie le flux JSON des citations lors du défilement, et récupérer les données directement sans analyser le HTML.
Outils : Python + requests + module json.
Livrable : Un script qui télécharge directement le JSON complet"""

import requests
import time
import json

HEADERS = {"User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
 "AppleWebKit/537.36 (KHTML, like Gecko) "
 "Chrome/140.0.0.0 Safari/537.36"),
     "Accept-Language": "fr-FR,fr;q=0.9"}

session = requests.Session()
session.headers.update(HEADERS)

def telecharger(session, url):
    """Télécharge une page. Renvoie le texte HTML, sinon None."""
    try:
        r = session.get(url, timeout=(5, 15), params={"page":page})
        r.encoding = 'utf-8'
        r.raise_for_status()
        return r
    except requests.exceptions.Timeout:
        print(f"[TIMEOUT] {url}")
    except requests.exceptions.HTTPError as e:
        print(f"[HTTP] {e.response.status_code} sur {url}")
    except requests.exceptions.RequestException as e:
        print(f"[RESEAU] {type(e).__name__} sur {url}")
        return None
    
url_base = "http://quotes.toscrape.com/api/quotes"
page = 1
quotes = []
continuer = True

while continuer:
    response = telecharger(session, url_base)
    data = response.json()
    quote = data['quotes']
    quotes.extend(quote)
    continuer = data["has_next"]
    page += 1
    time.sleep(1)

file_name = "quotes.json"

with open(file_name, "w", encoding="utf-8") as f:
    json.dump(quotes, f, indent=4, ensure_ascii=False)