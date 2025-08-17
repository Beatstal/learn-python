import random
import string

WORDS = [
    "python","tiger","elephant","pizza","guitar","holiday","weather",
    "keyboard","monitor","mountain","notebook","dolphin","panda","hangman"
]

def mask(word, guessed):
    return "".join(c if c in guessed else "_" for c in word)

def read_guess(used):
    while True:
        g = input("Guess a letter: ").strip().lower()
        if len(g) == 1 and g in string.ascii_lowercase and g not in used:
            return g
        print("Enter one new letter (a-z).")

def play(lives=6):
    word = random.choice(WORDS)
    guessed, wrong = set(), set()

    while True:
        display = mask(word, guessed)
        print(f"\nWord: {display}   Lives: {lives}   Wrong: {','.join(sorted(wrong)) or '-'}")

        if display == word:
            print("You win!")
            return
        if lives == 0:
            print(f"You lose! The word was: {word}")
            return

        g = read_guess(guessed | wrong)
        if g in word:
            guessed.add(g)
            print("✔ Correct")
        else:
            wrong.add(g)
            lives -= 1
            print("✘ Wrong")

if __name__ == "__main__":
    play()
