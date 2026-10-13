num = int(input("Enter the number: "))
isPrime = True

for i in range(2, num-1):
    if(num % i == 0):
        isPrime = False
        break
else:
    print("Not a Prime Number")

