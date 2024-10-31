#list ascending order
def sort_ascending(numbers):
    return sorted(numbers)

# list descending order
def sort_descending(numbers):
    return sorted(numbers, reverse=True)

if __name__ == "__main__":
    numbers = [5, 2, 9, 1, 5, 6]

    ascending_order = sort_ascending(numbers)
    print("Ascending Order:", ascending_order)

    descending_order = sort_descending(numbers)
    print("Descending Order:", descending_order)