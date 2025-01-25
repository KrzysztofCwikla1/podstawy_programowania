student_scores = [37, 51, 44, 23, 78, 92, 39, 84, 83, 51]

def min_pts(limit):
    return lambda pts: pts >= limit

# Example: Passing the minimum score of 70, 40, and 30
min_70 = filter(min_pts(70), student_scores)
min_40 = filter(min_pts(40), student_scores)
min_30 = filter(min_pts(30), student_scores)

print("Min 70 pts:", list(min_70))
print("Min 40 pts:", list(min_40))
print("Min 30 pts:", list(min_30))
