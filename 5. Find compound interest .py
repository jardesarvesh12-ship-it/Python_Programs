# # A = P(1 + R/100) t 
# # Compound Interest = A - P 

# # Taking Input from User
# p = int(input("Principal amount: "))
# r = int(input("Rate of interest: "))
# t = int(input("Time in years: "))

# a = p*(pow((1+r/100), t))
# CI = a - p
# print("Compound interest:", CI)



# # Using Built-in pow() Function ----> Instead of using the ** (exponent) operator, we can also use Python's pow() function.
# p = 10000
# r = 10.25
# t = 5
# amt = p*(pow((1+r/100), t))
# CI = amt - p

# Amt = p * (pow((1 + r / 100), t))
# CI = Amt - p



# # Using Exponentiation Operator
# P = 1200   
# R = 5.4    
# T = 2      
# A = P(1 + R/100) ** T
# CI = A - P
# print("compound interst is: ",CI)

