# zip combines two or more lists into pairs

names = ["Joha", "Sara"]
scores = [90, 85]

for name, score in zip(names, scores):
    print(name, "scored", score)
