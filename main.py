num1 = int(input())
num2 = int(input())
NOD = 0
NOK = 0
mult = num1 * num2
while (num1 != 0 and num2 != 0):
    if (num1 > num2):
        num1 = num1 % num2
    elif (num2 > num1):
        num2 = num2 % num1
if (num1 != 0):
    NOD = num1
else:
    NOD = num2
NOK = mult // NOD
print(NOD, NOK)