# Input the number of cricketers and their scores
n = int(input("Enter the number of cricketers: "))

# Lists to store cricketer names and scores
cricketer_names = []
scores = []

# Input cricketer names and scores
for i in range(n):
    name = input(f"Enter the name of cricketer {i + 1}: ")
    score = int(input(f"Enter the score for {name}: "))
    cricketer_names.append(name)
    scores.append(score)

# Find the cricketer with the highest score (Man of the Match)
max_score = max(scores)
index_of_max_score = scores.index(max_score)
man_of_the_match = cricketer_names[index_of_max_score]

# Find the cricketer with the lowest score
min_score = min(scores)
index_of_min_score = scores.index(min_score)
worst_cricketer_name = cricketer_names[index_of_min_score]

# Calculate the average score
average_score = sum(scores) / n

# Output the cricket statistics
print("\nCricket Scoreboard")
print("--------------------")
for i in range(n):
    print(f"{cricketer_names[i]:<20} : {scores[i]}")
print("--------------------")
print(f"Man of the Match: {man_of_the_match} (SCORE: {max_score})")
print(f"Worst Batsman: {worst_cricketer_name} (SCORE: {min_score})")
print(f"Average Score: {average_score:.2f}")
