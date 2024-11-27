import sys

def optimal_bst(keys, freq, n):
    cost = [[0 for x in range(n)] for y in range(n)]

    for i in range(n):
        cost[i][i] = freq[i]

    for L in range(2, n + 1):
        for i in range(n - L + 1):
            j = i + L - 1
            cost[i][j] = sys.maxsize

            for r in range(i, j + 1):
                c = (0 if r == i else cost[i][r - 1]) + (0 if r == j else cost[r + 1][j]) + sum(freq[i:j + 1])
                if c < cost[i][j]:
                    cost[i][j] = c

    return cost[0][n - 1]

n = 2
keys = [5, 6]
freq = [17, 25]

print("Хамгийн бага өртөг:", optimal_bst(keys, freq, n))
