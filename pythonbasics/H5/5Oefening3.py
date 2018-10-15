scores = []

print("Geef de scores voor de test. Gebruik -1 als je wilt afsluiten")

while True:
    score = float(input("score: "))
    if score == -1:
        break
    else:
        scores.append(score)

print("De scores in gesorteerde volgorde", sorted(scores, key=float), "\nHet gemiddelde van deze scores =", sum(scores) / len(scores))