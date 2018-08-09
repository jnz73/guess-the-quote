from scrape_quotes import get_quotes_list

print("webscraping quotes...")  # http://quotes.toscrape.com/
quote_list = get_quotes_list()

while True:
    print("playng game...")
    print(quote_list[0])
    while True:
        replay = input("Do you want to play again? (y/n): ")
        if replay in ("Y", "y", "N", "n"):
            break
    if replay not in ("Y", "y"):
        break
