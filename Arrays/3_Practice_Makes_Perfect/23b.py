
import TwThree

text = "An apple a day keeps the doctor away"

word_count = TwThree.count_words(text)
longest_first = TwThree.words_longest_first(text)
alphabetical_order = TwThree.words_alphabetically(text)

print("Text:", text)
print("Number of words:", word_count)
print("Words from the longest:", ", ".join(longest_first))
print("Words ordered alphabetically:", ", ".join(alphabetical_order))
