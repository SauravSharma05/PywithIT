my_list = [1, 2, 34,56]
# print(my_list[0]) 
# print(my_list[3]) 

len(my_list)

my_list[1] = 20 
my_list.append(6)  
my_list.remove(56)  

# print(my_list)


# for item in my_list:
    # print(item)
    # print(item + 5)


# n = 0
# while n < 5:
#     print(n)
#     n = n + 1 


# nested for loop 

# for i in range(3):
#     for j in range(2):
#         print(f'i: {i}, j: {j}')


# no do while in python


# if else condition 


# x1 = int(input("Please enter an integer: "))      // basic odd even 

# if x1 % 2 == 0:
#     print('even number')
# else:
#     print('odd number')


# list range 
# print(list(range(10,20)))


# print(sum(range(0,9)))

# number_list = [1,2,3,4,5,6,7]

# for val in number_list:
#     if val % 2 == 0:
#         print(f"even nos are : {val}")
#     else:
#         print(f"odd nos : {val}")


# def hello(2)
# def hello(num):               // similar to switch case
#     match num:
#         case 1:
#             return 1
#         case 2:
#             return 2
#         case _:
#             return 'nothing'

# for n in range(6,60):     //  here range does not included 6 and 60
#     for x in range(6,n):
#         if n % x == 0:
#             print(f"{n} equal to {x} * {n // x}")
#             break

# from enum import Enum
# class Numbr(Enum):
#     num1 = 1
#     num2 = 2
#     num3 = 3


# try:
#     user_input = int(input("Enter a number between 1 and 3: "))
    
#     if user_input < 1 or user_input > 3:
#         print("Please enter a number between 1 and 3.")
#     else:
#         numbe = Numbr(user_input)

#         match numbe:
#             case Numbr.num1:
#                 print('1')
#             case Numbr.num2:
#                 print('2')
#             case Numbr.num3:
#                 print('3')

# except ValueError:
#     print("Please enter a valid integer.")
# except Exception as e:
#     print(f"An error occurred: {e}")


