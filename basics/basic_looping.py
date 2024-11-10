def star_pattern(rows):
    for i in range(rows):
        for j in range(i + 1):
            print("*", end=" ")
        print()

star_pattern(5)

def triangle_star_pattern(rows):
    for i in range(rows, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print()

triangle_star_pattern(5)

# diamond 
def diamond_pattern(rows):
    for i in range(rows):
        print(" " * (rows - i - 1), end="")
        print("* " * (i + 1))
    
    for i in range(rows - 2, -1, -1):
        print(" " * (rows - i - 1), end="")
        print("* " * (i + 1))

diamond_pattern(5)


def invertednumbers(rows):
    for i in range(rows, 0, -1):
        for j in range(i):
            print(i, end=" ")
        print()

invertednumbers(5)