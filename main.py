while True:
    print("playng game...")
    while True:
        replay = input("Do you want to play again? (y/n): ")
        if replay in ("Y", "y", "N", "n"):
            break
    if replay not in ("Y", "y"):
        break


