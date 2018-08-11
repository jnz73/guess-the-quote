import requests
from quote import Quote
from bs4 import BeautifulSoup


def get_quotes_list():
    page = 1
    base_url = "http://quotes.toscrape.com"
    all_quotes = []
    while True:
        url = base_url + f"/page/{page}"
        print("Scraping " + url + "...")
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        quotes = soup.select(".text")
        for quote in quotes:
            text = quote.get_text()
            author = quote.find_next("small").get_text()
            details_url = quote.find_next("a")['href']
            response_details = requests.get(base_url + details_url)
            soup_details = BeautifulSoup(response_details.text, "html.parser")
            born_date = soup_details.select(".author-born-date")[0].get_text()
            born_location = soup_details.select(
                ".author-born-location")[0].get_text()
            birth = born_date + " " + born_location
            bio = soup_details.select(".author-description")[0].get_text()
            all_quotes.append(Quote(text, author, birth, bio))
        if not soup.select(".next"):
            break
        page += 1

    return all_quotes
