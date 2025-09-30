def exp(x, n):
    if n <= 0:
        return 1
    else:
        return x * exp(x, n-1)

#print(exp(3, 5))

def exp2(x, n):
    if n == 0:
        return 1
    elif n < 0 and n % 2 == 0:
        return (x**2)*((exp2(x,n+1))//2)
    elif n < 0 and n % 2 != 0:
        return x * (x**2) * ((exp2(x, n+1))//2)
    elif n > 0 and n % 2 == 0:
        return (x**2) * ((exp2(x, n-1))//2)
    elif n > 0 and n % 2 != 0:
        return x * (x**2) * ((exp2(x, n-1))//2)

#print(exp2(3, 4))

def exp3(x, n):
    if n <= 0:
        return 1
    elif n == 1:
        return x
    else:
        return x * x * exp(x, n-2)

#print(exp3(4, 3))
