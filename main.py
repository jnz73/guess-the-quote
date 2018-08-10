from scrape_quotes import get_quotes_list
from play_game import play
from quote import Quote

print("webscraping quotes...")  # http://quotes.toscrape.com/
quote_list = get_quotes_list()

while True:
    play(quote_list)
    while True:
        replay = input("Do you want to play again? (y/n): ")
        if replay in ("Y", "y", "N", "n"):
            break
    if replay not in ("Y", "y"):
        break
