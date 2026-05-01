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
    1 : CHARACTERS,
    2 : SPORTS
}

def getInput(used_set, rankings):
    for i in range(5):
            while not (1 <= rankings[i] <= 5) or rankings[i] in used_set:
                print("Available Ranks: " + str({1, 2, 3, 4, 5} - used_set)[1:-1])
                user_in = input(str(i + 1) + ": ")
                if len(user_in) != 1 or user_in == ' ': continue
                rankings[i] = int(user_in)
            used_set.add(rankings[i])

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

        while not (1 <= cat <= 2):
            user_in = input("Pick Category: ")
            if len(user_in) != 1 or user_in == ' ': continue
            cat = int(user_in)

        options = random.sample(Categories[cat], 5)
        print("\nRank:")
        for i in range(5):
            print(str(i + 1) + ": " + options[i])

        print("\nPlayer 1:")
        p1_used_ranks = set()
        getInput(p1_used_ranks, p1_rankings)

        print("\nPlayer 2:")
        p2_used_ranks = set()
        getInput(p2_used_ranks, p2_rankings)

        print("\nGuess Ranking:")

        print("\nPlayer 1:")
        p1_used_guesses = set()
        getInput(p1_used_guesses, p1_guesses)

        print("\nPlayer 2:")
        p2_used_guesses = set()
        getInput(p2_used_guesses, p2_guesses)

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