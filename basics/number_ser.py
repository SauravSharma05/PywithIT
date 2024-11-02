# number series
def print_number_series(n):
    series = []
    
    for i in range(1, n + 1):
        series.append(i)  
        if i < n:
            print(i, end=" + ")
        else:
            print(i, end=" ")  
    
    total_sum = sum(series)
    print(f"= {total_sum}")

if __name__ == "__main__":
    n = int(input("Enter a number: "))  
    print_number_series(n)  