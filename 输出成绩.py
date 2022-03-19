n = int(input())
scores = []
for i in range(n):
    scores.append(int(input()))
ave = sum(scores) / len(scores)
print(f"{ave:.3f}")
for score in scores:
    if score > ave:
        print(score)
