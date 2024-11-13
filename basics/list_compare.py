from collections import Counter

list1 = [1, 2, 3, 3]
list2 = [3, 2, 1]

# Compare using Counter
print(Counter(list1) == Counter(list2))  



list1 = [1, 2, 3]
list2 = [2, 3, 4]

diff = [x for x in list1 if x not in list2]
print(diff) 

list1 = [5, 3, 1]
list2 = [1, 5, 3]

# Sort and compare
print(sorted(list1) == sorted(list2))  