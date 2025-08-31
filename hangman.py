import random

# Step 1: Word list
words = ["roy","sai","mojesh","tharun","rakesh","yogesh."]
word = random.choice(words)
guessed = []
attempts = 6

print("🎯 Hangman Game! Guess the word.")

# Step 3: Game loop
while attempts > 0:
    # Show current guessed word
    display = "".join([letter if letter in guessed else "_" for letter in word])
    print("\nWord:", display)

    # Win check
    if display == word:
        print("🎉 You win! The word was:", word)
        break

    guess = input("Guess a letter: ").lower()

    if guess in guessed:
        print("⚠ Already guessed!")
    elif guess in word:
        guessed.append(guess)
        print("✅ Correct!")
    else:
        guessed.append(guess)
        attempts -= 1
        print("❌ Wrong! Attempts left:", attempts)

# Lose check
if attempts == 0:
    print("💀 Game Over! The word was:", word)