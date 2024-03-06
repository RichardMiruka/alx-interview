#To solve this problem, we can simulate the tournament rounds, 
# keeping track of the players' progress and the round in which they get eliminated.
# It iteratively plays rounds until there are only two players left, updating the rounds array accordingly.
# The result is an array indicating the last round in which each player participates.
# This solution assumes the input skills array is non-empty and contains at least two players.

def solution(skills):
    n = len(skills)
    rounds = [0] * n  # Initialize rounds array with zeros

    def play_round(players):
        winners = []
        for i in range(0, len(players), 2):
            player1, player2 = players[i], players[i + 1]
            winner = player1 if skills[player1] > skills[player2] else player2
            winners.append(winner)
            rounds[winner] += 1
        return winners

    players = list(range(n))

    while len(players) >= 2:
        players = play_round(players)

    return rounds

# Example usage:
skills = [4, 2, 7, 1, 5, 3, 8, 6]
result = solution(skills)
print(result)
