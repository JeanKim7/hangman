import random

# A game of hangman


def position_correct_letter(letter, word):
    indices = []
    position = -1
    for i in range(len(word)):
        if letter == word[i]:
            indices.append(i)
    return indices

def generate_word():
    word_string = "hospital reinforce glove article recognize identity process bargain practical publication cooperative important prosper shatter bed yard game cable stock toss dish democratic thank impound jungle"
    word_list = word_string.split()
    answer = random.choice(word_list)

    blank_list =["_" for a in range(len(answer))]
    blank_template = "".join(blank_list)


def hangman():
    word_string = "hospital reinforce glove article recognize identity process bargain practical publication cooperative important prosper shatter bed yard game cable stock toss dish democratic thank impound jungle"
    word_list = word_string.split()
    answer = random.choice(word_list)

    blank_list =["_" for a in range(len(answer))]
    blank_template = "".join(blank_list)
    
    tries = 8

    used_letters = []

    for i in range(1, 9):
        print(blank_template)
        print(f"Tries left: {tries}")
        print(f"Letters used: {used_letters}")
        guess = input("Enter a guess for the letter: ").lower()
        while (len(guess) != 1 and guess in used_letters):
            guess = input("Enter only ONE letter that you have NOT USED: ").lower()
        if guess not in answer:
            used_letters.append(guess)
            print("Sorry, that letter isn't in the word!")
            tries -= 1
        else:
            indices = position_correct_letter(guess, answer)
            for i in indices:
                blank_list[i] = guess
            tries -=1
            print("That letter is in the word!")
            if blank_template == answer:
                print(f"Congratulations, you won in {tries} tries! The answer is {answer}.")
                break

    print("Game Over! You ran out of tries")




hangman()

