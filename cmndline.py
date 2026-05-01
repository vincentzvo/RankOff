stuff = {
    1 : "Luffy",
    2 : "Zoro",
    3 : "Nami",
    4 : "Usopp",
    5 : "Sanji"
}

p1_rankings = [0, 0, 0, 0, 0]
p1_guesses = [0, 0, 0, 0, 0]
p2_rankings = [0, 0, 0, 0, 0]
p2_guesses = [0, 0, 0, 0, 0]

print(
    "\nRank:" + "\n1: " + stuff[1]
              + "\n2: " + stuff[2]
              + "\n3: " + stuff[3]
              + "\n4: " + stuff[4]
              + "\n5: " + stuff[5]
              + "\n"
)

print("Player 1:")
p1_rankings[0] = input("1: ")
p1_rankings[1] = input("2: ")
p1_rankings[2] = input("3: ")
p1_rankings[3] = input("4: ")
p1_rankings[4] = input("5: ")

print("\nPlayer 2:")
p2_rankings[0] = input("1: ")
p2_rankings[1] = input("2: ")
p2_rankings[2] = input("3: ")
p2_rankings[3] = input("4: ")
p2_rankings[4] = input("5: ")

print("\nGuess Ranking:")

print("\nPlayer 1:")
p1_guesses[0] = input("1: ")
p1_guesses[1] = input("2: ")
p1_guesses[2] = input("3: ")
p1_guesses[3] = input("4: ")
p1_guesses[4] = input("5: ")

print("\nPlayer 2:")
p2_guesses[0] = input("1: ")
p2_guesses[1] = input("2: ")
p2_guesses[2] = input("3: ")
p2_guesses[3] = input("4: ")
p2_guesses[4] = input("5: ")

p1_score = 0
p2_score = 0
for i in range(5):
    if p1_guesses[i] == p2_rankings[i]:
        p1_score += 1
    if p2_guesses[i] == p1_rankings[i]:
        p2_score += 1

print("\nPlayer 1 Score: " + str(p1_score))
print("\nPlayer 2 Score: " + str(p2_score))