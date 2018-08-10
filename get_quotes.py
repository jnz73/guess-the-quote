from scrape_quotes import get_quotes_list
from os.path import exists
from pathlib import Path
import pickle

def get_quotes():
    file_is_valid = False
    quote_list = []
    file = Path("quotes.pickle")
    if exists(file):
        with open(file, "rb") as file:
            quote_list = pickle.load(file)
            if len(quote_list) > 0:
                print("file is valid, loading quotes...")
                file_is_valid = True
            else:
                print("file is not valid")
    else:
        print("no quotes file found")
    if not file_is_valid:
        print("webscraping quotes...")  # http://quotes.toscrape.com/
        quote_list = get_quotes_list()
        with open(file, "wb") as file:
            pickle.dump(quote_list, file)
    return quote_list
