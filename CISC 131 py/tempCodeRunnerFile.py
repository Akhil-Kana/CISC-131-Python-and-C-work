def wallis(iteration):
    estimate = 2.0
    for i in range(1, iteration):
        n = (2 * i) / (2 * i - 1)
        d = (2 * i) / (2 * i + 1)
        estimate *= (n * d)
    return estimate

print(wallis(2))
print(wallis(10000000))
