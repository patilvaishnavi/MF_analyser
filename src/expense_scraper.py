# src/expense_scraper.py

import requests
from bs4 import BeautifulSoup
import re

def get_expense_ratio(url: str) -> float:
    """
    Scrape the mutual fund's expense ratio from the given Groww URL.
    Returns the ratio as a float (e.g., 0.75).
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; ExpenseScraper/1.0)"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.RequestException as e:
        raise RuntimeError(f"Failed to fetch URL: {e}")

    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.get_text(separator=" ")

    match = re.search(r'Expense ratio\s*[:\-]?\s*([\d.]+)%', text, re.IGNORECASE)

    if match:
        return float(match.group(1))  # convert string to float
    else:
        raise ValueError("Expense ratio not found in page text.")
