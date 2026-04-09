

# # Using math.factorial()
# import math
# n = 8
# print(math.factorial(n))



# #  while loop
# num = int(input("enter a number: "))
# fact = 1

# a = 1
# while a <= num :
#     fact = fact * a
#     a = a+1
# print("Factorial of", num, "is ", fact  )



# # For loop
# n = 6
# if n < 0:
#     print("number is negative or an zero ")
# else:
#     f = 1 
#     for i in range(1,n+1):
#         f *= i
#         print(f)




# # Using a Recursive Function
# def fact(n):
#     if n < 0:
#         return "Factorial is not defined for negative numbers"
#     return 1 if n <= 1 else n * fact(n-1)

# print(fact(6))  
# print(fact(-3))
