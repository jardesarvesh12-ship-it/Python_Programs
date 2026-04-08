num = int(input("enter a number: "))
temp = num
sum = 0


while temp > 0:
    # Obtain Last Digit e.g 153---> output 3
    digit = temp % 10
    # Find power of digit
    cube = digit **  3
    # Increament 
    sum = sum + cube
    # 
    temp //= 10

if sum == num:
    print("Armstring number: ")
else: 
    print("Not-Armstring number: ")



