sentence = "I completely agree with you"

# Calculate number of letters in each word using anonymous function
result = list(map(lambda word: len(word), sentence.split()))

print(f"Text: {sentence}")
print(f"No. of letters in words: {result}")
