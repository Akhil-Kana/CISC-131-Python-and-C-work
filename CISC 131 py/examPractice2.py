"""
def sForm(length, width):
    print("The area is {:.1f} X {:.1f}.".format(length, width))

sForm(23.54376910, 5.789810)
"""

"""

(A)

for a in range(1, 4):
    for b in range(2):
        print(a + b, end="")

ans:
122334

(B)

board = [['a', 'b', 'c'], ['d', 'e', 'f']]
baord.append(['g', 'g', 'i'])
board.pop(0)
print(baord[0][2] + board[1][1])

ans:
fh
"""

"""
sl = "halloween"

(A)

print(sl*2)

ans:
halloweenhalloween

(B)

print(sl[2:])

ans:
lloween

(C)

sl.capitalize()
print(sl[-1])
print(sl[0])

ans:

n
h
"""

"""
my_list = [3,1,2]
x = my_list
y = my_list[:]
z = my_list.sort()

x.append(4)
y.pop(1)
print(x)
print(y)
print(z)

ans:
[1,2,3,4]
[3,2]
None

"""

"""
def occursMult(lst, target):
    for i in range(len(lst)):
        if lst.count(target) > 1:
            return True
    return False

print(occursMult(([1,2,3,2,2,4]), 2)) --> returns True
print(occursMult(([1,2,3,2,2,4]), 1)) --> returns False
"""