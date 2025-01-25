jump_scores = [(17,15,16,17,15),
               (16,18,19,17,19),
               (19,15,15,19,18),
               (18,17,19,15,16)]

# Calculate total score for each competitor (excluding the highest and lowest scores)
total_scores = list(map(lambda scores: sum(scores) - min(scores) - max(scores), jump_scores))
print(total_scores)
