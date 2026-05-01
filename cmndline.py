CHARACTERS = [
    "Luffy",
    "Zoro",
    "Nami",
    "Usopp",
    "Sanji",
    "Chopper",
    "Robin",
    "Franky",
    "Brook"
]

SPORTS = [
    "Soccer",
    "Basketball",
    "Baseball",
    "American Football",
    "Tennis",
    "Track",
    "Volleyball",
    "Table Tennis",
    "Bowling",
    "Darts"
]

def main():
    p1_score = 0
    p2_score = 0

    while p1_score < 10 and p2_score < 10 or p1_score == p2_score:
        p1_rankings = [0, 0, 0, 0, 0]
        p1_guesses = [0, 0, 0, 0, 0]
        p2_rankings = [0, 0, 0, 0, 0]
        p2_guesses = [0, 0, 0, 0, 0]

        print(
            "\nRank:" + "\n1: " + CHARACTERS[1]
                    + "\n2: " + CHARACTERS[2]
                    + "\n3: " + CHARACTERS[3]
                    + "\n4: " + CHARACTERS[4]
                    + "\n5: " + CHARACTERS[5]
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

        for i in range(5):
            if p1_guesses[i] == p2_rankings[i]:
                p1_score += 1
            if p2_guesses[i] == p1_rankings[i]:
                p2_score += 1

        print("\nPlayer 1 Score: " + str(p1_score))
        print("Player 2 Score: " + str(p2_score))

        if p1_score >= 10 and p1_score == p2_score:
            print("\nSudden Death")
    
    if p1_score > p2_score:
        print("\nPlayer 1 Wins")
    else:
        print("\nPlayer 2 Wins")

if __name__ == "__main__":
    main()