#user input for amount of lottery and drawn balls
lotteryballs = int(input("Enter the total number of lottery balls: "))
drawnballs = int(input("Enter the number of the drawn balls: "))

#Calculation
lower = (lotteryballs - drawnballs)

#Gets factorial of a number
def factorial(n):
    fact = 1  
    for num in range(2, n + 1):
        fact *= num
    return fact

#Check if lotteryballs and drawnballs number is higher than zero and checks if
#there are more lottery balls than drawn balls
#If all is fine calculates the probability using the formula factorial function
def probability(lotteryballs, drawnballs):
    if lotteryballs > 0 and drawnballs > 0 and lotteryballs > drawnballs:
        chance = factorial(lotteryballs) / (factorial(lower)*factorial(drawnballs))
        print("The probability of of guessing all " + str(drawnballs) + " balls correctly is 1/" + str(int(chance)))
    elif drawnballs > lotteryballs:
        print("Lottery balls value needs to be higher than drawn balls value")
    else:
        print("Number of balls must be a positive number")

#Calling the function
probability(lotteryballs, drawnballs)
