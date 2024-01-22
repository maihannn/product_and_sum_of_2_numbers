# Name: Jamaica C. Palillo
# Section: BSCPE 1-5

# Exercise 1: Calculate the multiplication and sum of two numbers.

# If the answer is equal or less than 1000, get the product.
# If not, get their sum.


# get the two integers

number1 = int(input("Enter the First Number: "))
number2 = int(input("Enter the Second Number: "))


def get_answer (number1, number2):
    
    product = number1*number2
    
    if (product <= 1000):
        return product
        
    else:
        return number1 +number2


answer = get_answer (number1, number2)
print ("\nThe answer is: ", answer)
        



