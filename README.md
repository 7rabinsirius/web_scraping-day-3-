# web_scraping-day-3-Sure, Rabin! Here's a concise and clear README you can include with your BBC News headlines scraper:

---

# 📰 BBC News Headlines Scraper

This Python script fetches the latest headlines from the [BBC homepage](https://www.bbc.com/) and writes them into a text file.

## Features
- Scrapes headlines marked with `data-testid="card-headline"`
- Saves the results in `news.txt`
- Handles request errors gracefully

## Requirements
- Python 3.x
- Libraries:
  - `requests`
  - `beautifulsoup4`
  - `html5lib`

Install dependencies with:

```bash
pip install requests beautifulsoup4 html5lib
```

## Usage

Simply run the script:

```bash
python bbc_headlines_scraper.py
```

The extracted headlines will be saved to `news.txt` in the same directory.

---


