#Determining whether a number is prime or composite with O(1)
#ALGORITHM: If a number is not divisible by 2,3,5 and 7 then it a prime
num = int(input("Enter a number : "))
if num == 2 or num == 3 or num == 5 or num == 7:
    print(num,"is prime")
elif num%2 != 0 and num%3 != 0 and num%5 != 0 and num%7 != 0:
    print(num,"is prime")
else:
    print(num,"is composite")
