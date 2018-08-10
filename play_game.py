from random import choice


def play(quote_list):
    guesses = 4
    found = False
    selected_quote = choice(quote_list)
    print("Here is a Quote:")
    print("\n")
    print(selected_quote.quote)
    print("\n")
    while guesses > 0 and not found:
        print_hint(guesses, selected_quote)
        answer = input(
            f"Who said this? ({guesses} guesses remaining): ")
        if answer.lower() == selected_quote.author.lower():
            print("You guessed correctly! Congratulations!")
            found = True
        else:
            print("Sorry wrong answer!")
            guesses -= 1
    if not found:
        print(f"The author was: {selected_quote.author}! Better luck next time!")

def print_hint(guesses, selected_quote):
    prefix = "Here's a hint: The author "
    if guesses == 2:
        print(prefix + f"was born in {selected_quote.birth}")
    if guesses == 1:
        print(prefix + f"initials are {selected_quote.get_initials()}")
    if guesses == 0:
        print(prefix + f"bio is:\n\n{selected_quote.bio_without_author_name()}")