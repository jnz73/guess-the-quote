from scrape_quotes import get_quotes_list
from play_game import play
from quote import Quote
from os.path import exists
from pathlib import Path
import pickle

file_is_valid = False
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

while True:
    play(quote_list)
    while True:
        replay = input("Do you want to play again? (y/n): ")
        if replay in ("Y", "y", "N", "n"):
            break
    if replay not in ("Y", "y"):
        break
