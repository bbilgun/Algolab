def aggregate_cost(n):
    total_cost = 0

    for i in range(1, n + 1):
        if (i & (i - 1)) == 0:
            total_cost += i
        else:
            total_cost += 1

    return total_cost

n = 16
print(f"Нийт өртөг (n = {n}): {aggregate_cost(n)}")
