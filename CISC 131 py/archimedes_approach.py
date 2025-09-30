import math

num_sides = 12
def archimedes(num_sides):
    if num_sides < 3:
        return 0
    else:
        half_angle = 360/num_sides/2
        s_len = math.sin(math.radians(half_angle))
        perimeter = s_len*(num_sides*2)
        pi = perimeter/2
        return pi

print(archimedes(num_sides))

def archimedes2(low, high):
    print("n  |  pi")
    print("--------")
    for i in range(low, high+1):
        print(str(i) + "  |  " + str(archimedes(i)))

print(archimedes2(3, num_sides))
