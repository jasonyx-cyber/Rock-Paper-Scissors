import random

worsds = ["python", "developer", "keyboard", "backend"]

word = random.choice(worsds)
scrambled = list(word)
random.shuffle(scrambled)
scrambled_word = ''.join(scrambled)

print("unscramble the word:", scrambled)

attempts = 3

while attempts > 0:
    guess = input("Your guess: ").lower()
    if guess == word:
        print("Correct!")
        break
    else:
        attempts -= 1
        print("Wrong! Attempts left:", attempts)
        if attempts == 0:
            print("Game over! The word was:", word)
    