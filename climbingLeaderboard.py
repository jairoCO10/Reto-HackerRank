#
# Complete the 'climbingLeaderboard' function below.
#  https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem
#  ralizado por Jairo Cogollo
#  mickt681@gmail.com

# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbing_leaderboard(ranked, player):
    unique_ranked = sorted(set(ranked), reverse=True)
    i = len(unique_ranked) - 1
    result = []
    for score in player:
        while i >= 0 and score >= unique_ranked[i]:
            i -= 1
        if i == -1:
            result.append(1)
        else:
            result.append(i + 2)
    return result

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    rankedCount = int(input("ranked count ").strip())

    ranked = list(map(int, input("ranked ").rstrip().split()))

    playerCount = int(input("player count").strip())

    player = list(map(int, input().rstrip().split()))

    # ranked_count = 7
    # ranked = [100, 100, 50, 40, 40, 20, 10]
    # player_count = 4
    # player = [5, 25, 50, 120]

    result = climbing_leaderboard(ranked, player)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
    
    print(result)
