def letter_checker(word, letter):
    """the method letter_checker checks if the letter guessed is in the word"""
    i = 0
    spot_in_word = []
    for index in word:
        if letter == index:
            spot_in_word += [i]
        i += 1

    return spot_in_word


word = input("Enter the word your opponent will be trying to guess: ")
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")  # Used to hide word from person guessing it
max_number_of_guesses = 6
num_guesses = 0
num_letters = len(word)
progress = ["_"] * num_letters
out_of_loop = 0
wrong_msg_tick = 0
while num_guesses != max_number_of_guesses:
    letter = input("Guess a letter you: ")
    if letter_checker(word, letter) != []:
        for i in letter_checker(word, letter):
            progress[i] = letter
            out_of_loop += 1
        print(progress)
    else:
        num_guesses += 1
        wrong_msg_tick += 1
        print("You have " + str(max_number_of_guesses - num_guesses) + " guesses left")

    if out_of_loop == len(progress):
        num_guesses = max_number_of_guesses
        print("Congratz! You guessed " + word + " correctly")

    if wrong_msg_tick == max_number_of_guesses:
        print("You LOSE! The correct word was: " + word)
