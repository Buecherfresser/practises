row = int(input("welche reihe?")) - 1
dreieck = [1, 1]
print(dreieck)
for i in range(row):
    dreieckneu = []
    for r in range(len(dreieck)-1):
        dreieckneu.append(dreieck[r] + dreieck[r + 1])
    dreieckneu.insert(0, 1)
    dreieckneu.append(1)
    dreieck = dreieckneu
    print(dreieck)