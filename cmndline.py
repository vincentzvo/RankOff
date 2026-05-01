stuff = {
    1 : "Luffy",
    2 : "Zoro",
    3 : "Nami",
    4 : "Usopp",
    5 : "Sanji"
}

rankings = [0, 0, 0, 0, 0]
guesses = [0, 0, 0, 0, 0]

print(
    "\nRank:" + "\n1: " + stuff[1]
              + "\n2: " + stuff[2]
              + "\n3: " + stuff[3]
              + "\n4: " + stuff[4]
              + "\n5: " + stuff[5]
              + "\n"
)

rankings[0] = input("1: ")
rankings[1] = input("2: ")
rankings[2] = input("3: ")
rankings[3] = input("4: ")
rankings[4] = input("5: ")

print("\nGuess Ranking:")
guesses[0] = input("1: ")
guesses[1] = input("2: ")
guesses[2] = input("3: ")
guesses[3] = input("4: ")
guesses[4] = input("5: ")

score = 0
for i in range(5):
    if rankings[i] == guesses[i]:
        score += 1
print("\nScore: " + str(score))