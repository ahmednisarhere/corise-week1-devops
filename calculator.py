# add
def add(a,b):
    return a + b
# subtraction
def sub(a,b):
    return a - b
# Multiplication
def mul(a,b):
    return a*b
# division
def div(a,b):
    if b == 0:
        print("Error: Division by zero is not allowed.")
    else:
        return a / b

if __name__ == "__main__":
    a = 4
    b = 5
    print("Sum of " + str(a) + " and " + str(b) + " is ", add(a,b))
    print("Difference of " + str(a) + " and " + str(b) + " is ", sub(a,b))
    print("Product of " + str(a) + " and " + str(b) + " is ", mul(a,b))
    print("Division of " + str(a) + " and " + str(b) + " is ", div(a,b))
    