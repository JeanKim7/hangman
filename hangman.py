import random
from hangman_pic import hangman_picture

# A game of hangman


def position_correct_letter(letter, word):
    indices = []
    for i in range(len(word)):
        if letter == word[i]:
            indices.append(i)
    return indices

def choose_random_word():
    word_string = "hospital reinforce glove article recognize identity process bargain practical publication cooperative important prosper shatter bed yard game cable stock toss dish democratic thank impound jungle fat crouch assumption pop age candidate nut we disgrace official choice conservation dorm miracle glow twilight gold tender ban anticipation diameter fibre wear suffering salon license solution turkey garage dine restoration effective discrimination bush economics blow look alarm concept flu flex defend electronics enhance hear timber resist site district tenant"
    word_list = word_string.split()
    return random.choice(word_list)


def hangman():
    answer = choose_random_word()

    blank_list =["_" for a in range(len(answer))]
    blank_template = "".join(blank_list)
    
    tries = 7

    used_letters = []

    for i in range(1, (7+len(answer))):
        if tries == 0:
            hangman_picture((7-tries))
            print(f"Game Over! You ran out of tries. The answer is '{answer}'")
            break
        hangman_picture((7-tries))
        print(f"\n\t{blank_template}\t\tlength = {len(answer)}\n")
        print(f"Tries left: {tries}")
        print(f"Letters used: {used_letters}")
        guess = input("Enter a guess for the letter: ").lower()
        while (guess.isdigit() == True or len(guess) != 1 or guess in used_letters):
            guess = input("Enter only ONE letter that you have NOT USED: ").lower()
        if guess not in answer:
            used_letters.append(guess)
            print("Sorry, that letter isn't in the word!")
            tries-=1

        else:
            indices = position_correct_letter(guess, answer)
            for i in indices:
                blank_list[i] = guess
                blank_template = "".join(blank_list)
            print("That letter is in the word!")
            if blank_template == answer:
                print(f"\nCongratulations, you won!!! The answer is '{answer}'.")
                break





hangman()