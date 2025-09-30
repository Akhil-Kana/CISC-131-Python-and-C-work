def newtons(x, iteration):
    current_guess = x/2
    for i in range(iteration): # can also be (1, iteration + 1) and (0, iteration)
        current_guess = (current_guess + (x/current_guess))/2
    return current_guess

print(newtons(3, 10000))
