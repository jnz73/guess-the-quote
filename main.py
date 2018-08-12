from get_quotes import get_quotes
from play_game import play


while True:
    play(get_quotes())
    while True:
        replay = input("Do you want to play again? (y/n): ")
        if replay in ("Y", "y", "N", "n"):
            break
    if replay in ("N", "n"):
        break
