# Web Scraper

A collection of Python web scraping projects focused on extracting, processing, and storing structured data from static websites and web APIs.

The repository demonstrates two primary scraping methodologies: traditional **HTML parsing** for static pages and direct **JSON API consumption** for dynamically loaded content.

---

## Projects Summary

### 01 — Books Web Scraper

A static catalog scraper for [Books to Scrape](https://books.toscrape.com/) designed to extract structured product information across multiple paginated pages.

* **Data Extraction:** Scrapes all 50 catalog pages to collect **1,000 unique book records**.
* **Fields Collected:** Title, price, stock availability, and rating.
* **Request Management:** Utilizes `requests.Session()` to reuse TCP connections, with explicit timeouts and exception handling.
* **Parsing Engine:** Uses `BeautifulSoup` paired with `lxml` parser for rapid DOM traversal.
* **Data Pipeline:** Cleans and formats extracted fields into a `pandas.DataFrame` before exporting to Excel.

**Tech Stack:** `Python` `Requests` `BeautifulSoup4` `lxml` `Pandas` `OpenPyXL`

---

### 02 — Quotes API Scraper

An API-based data extractor targeting the backend service behind the dynamic pages of Quotes to Scrape.

* **Direct API Consumption:** Bypasses DOM parsing by inspecting network activity and querying the underlying JSON API endpoint directly.
* **Dynamic Pagination:** Implements continuous pagination driven by response metadata (`has_next`).
* **Session & Rate Control:** Reuses persistent sessions with built-in delays (`time.sleep`) to prevent server overload and manage HTTP status codes.
* **Data Aggregation:** Aggregates structured objects into memory and exports the final dataset as JSON.

**Tech Stack:** `Python` `Requests` `JSON` `REST API`

## Project Structure

```text
Web-scraper/
│
├── 01_books_toscrape/
│   ├── scraper.py
│   └── ...
│
├── 02_quotes_api/
│   ├── scraper.py
│   └── ...
│
├── requirements.txt
└── README.md

```

---

## Installation & Setup

1. **Clone the repository:**
```bash
git clone [https://github.com/Mob73/Web-scraper.git](https://github.com/Mob73/Web-scraper.git)
cd Web-scraper

```


2. **Create and activate a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

```


3. **Install dependencies:**
```bash
pip install -r requirements.txt

```



---

## Running the Projects

Run either script directly from the root directory:

* **Execute Books Scraper:**
```bash
python 01_books_toscrape/scraper.py

```


* **Execute Quotes API Scraper:**
```bash
python 02_quotes_api/scraper.py

```



---

## Scraping Methodologies

### 1. HTML Scraping (Static Pages)

```text
Target Site  ──►  HTTP Request  ──►  HTML Response
                                          │
                                BeautifulSoup / lxml
                                          │
                                 Structured Data
                                          │
                                    Pandas Clean
                                          │
                                    Excel Export

```

### 2. API-Based Extraction (Dynamic Pages)

```text
DevTools Analysis  ──►  Identify Endpoint  ──►  HTTP Request
                                                     │
                                               JSON Response
                                                     │
                                            Pagination (has_next)
                                                     │
                                              Structured Data
                                                     │
                                                JSON Export

```

---

## Robustness & Error Handling

Both projects incorporate defensive techniques to maintain stability:

* **Timeouts:** All HTTP requests specify non-blocking timeouts to prevent hanging indefinitely.
* **Exception Handling:** Custom catching for connection failures, HTTP status codes, and DNS issues using `try-except` blocks.
* **Connection Pooling:** `requests.Session()` reduces request overhead and handles header persistence.

---

## Key Skills Demonstrated

* Python HTTP session management (`requests.Session`)
* DOM traversal with BeautifulSoup and `lxml`
* Frontend API reverse-engineering via Browser DevTools
* Handling API pagination without fixed page numbers
* Data cleaning, transformation, and structured export with Pandas

---

## Disclaimer

These projects are intended strictly for educational and experimentation purposes using public sandbox sites designed for scraping practice. Always respect target website `robots.txt`, terms of service, and rate limits.

---

## Author

**Moubarak Djato**

* **GitHub:** [@Mob73](https://github.com/Mob73)
