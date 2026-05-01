import random

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

Categories = {
    "1" : CHARACTERS,
    "2" : SPORTS
}

def main():
    p1_score = 0
    p2_score = 0

    while p1_score < 10 and p2_score < 10 or p1_score == p2_score:
        p1_rankings = [0, 0, 0, 0, 0]
        p1_guesses = [0, 0, 0, 0, 0]
        p2_rankings = [0, 0, 0, 0, 0]
        p2_guesses = [0, 0, 0, 0, 0]

        cat = 0
        print("\nCategories:\n1: Characters\n2: Sports\n")
        cat = input("Pick Category: ")

        options = random.sample(Categories[cat], 5)
        print("\nRank:")
        for i in range(5):
            print(str(i + 1) + ": " + options[i])

        print("\nPlayer 1:")
        for i in range(5):
            p1_rankings[i] = input(str(i + 1) + ": ")

        print("\nPlayer 2:")
        for i in range(5):
            p2_rankings[i] = input(str(i + 1) + ": ")

        print("\nGuess Ranking:")

        print("\nPlayer 1:")
        for i in range(5):
            p1_guesses[i] = input(str(i + 1) + ": ")

        print("\nPlayer 2:")
        for i in range(5):
            p2_guesses[i] = input(str(i + 1) + ": ")

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