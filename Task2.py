number = int(input("Enter a number : "))

while number < 10 or number > 100 :
    print("Error! Please enter a number between 10 and 100")
    print("Valid number ", number)
    number = int(input("Enter a number again: "))

fizzCount = 0
buzzCount = 0
fizzBuzzCount = 0


for i in range(number):
    if i % 3 == 0 & i % 5 == 0:
        print("FizzBuzz")
        fizzBuzzCount += 1
        print("FizzBuzz count : ", fizzBuzzCount)
    elif i % 3 == 0:
        print("Fizz")
        fizzCount += 1
        print("Fizz count : ", fizzCount)
    elif i % 5 == 0:
        print("Buzz")
        buzzCount += 1
        print("Buzz count : ", buzzCount)
    elif i % 7 == 0:
        continue
    else:
        print(i)




