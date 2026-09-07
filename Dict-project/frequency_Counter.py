# Ek sample text/sentence
sentence = "python is easy and python is powerful python"

# Sentence ko space ke basis par alag-alag words me todna (List ban jayegi)
words = sentence.split()

# Empty dictionary frequency store karne ke liye
word_count = {}

# Loop se har ek word ko check karenge
for word in words:
    if word in word_count:
        word_count[word] += 1  # Agar word pehle se hai, toh 1 bada do
    else:
        word_count[word] = 1   # Agar naya word hai, toh entry start karo

# Result print karte hain
print("=== WORD FREQUENCY ===")
for word, count in word_count.items():
    print(f"'{word}': {count} baar aaya hai")