import requests
from bs4 import BeautifulSoup

URLS = {
    "refund": "https://anderbaher.in/refund_returns/",
    "privacy": "https://anderbaher.in/privacy-policy/",
    "terms": "https://anderbaher.in/tmc/"
}

def scrape():
    for name, url in URLS.items():
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        text = soup.get_text(separator="\n")

        with open(f"faq/{name}.txt", "w", encoding="utf-8") as f:
            f.write(text)

        print(f"[OK] Saved faq/{name}.txt")

if __name__ == "__main__":
    scrape()

