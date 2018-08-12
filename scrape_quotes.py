import requests
from quote import Quote
from bs4 import BeautifulSoup


def scrape_quotes_list():
    page = 1
    BASE_URL = "http://quotes.toscrape.com"
    all_quotes = []
    while True:
        url = BASE_URL + f"/page/{page}"
        print("Scraping page " + page + "...")
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        quotes = soup.select(".text")
        for quote in quotes:
            text = quote.get_text()
            author = quote.find_next("small").get_text()
            details_url = quote.find_next("a")['href']
            response_details = requests.get(BASE_URL + details_url)
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
