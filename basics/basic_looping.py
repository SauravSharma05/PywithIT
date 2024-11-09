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