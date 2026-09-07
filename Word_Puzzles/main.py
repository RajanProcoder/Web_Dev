# main.py

import random
# Step A: words_data file se words_list ko import karna
from words_data import words_list

# Step B: List me se Random Word choice karna
secret_word = random.choice(words_list)

# Step C: Word (String) ko List me Convert karna
word_letters = list(secret_word)

# Step D: List ke letters ko Shuffle (Mix) karna
random.shuffle(word_letters)

# Step E: Shuffled List ko wapas String me Join karna
jumbled_word = "".join(word_letters)

# --- GAME INTERFACE ---
print("=" * 40)
print("🎯 ADVANCED WORD SCRAMBLE GAME 🎯")
print("=" * 40)
print(f"Jumbled Word : {jumbled_word}")
print("=" * 40)

# User Guess
user_guess = input("Sahi Word Guess Kijiye: ").lower()

if user_guess == secret_word:
    print(f"🎉 BINGO! Aapka Jawab Bilkul Sahi Hai! 👉 '{secret_word}'")
else:
    print(f"❌ Galat Jawab! Sahi Word tha: '{secret_word}'")
