
# **************************************************************************************************************************************
# **************************************************************************************************************************************

# def a():
#     dgt_1 = int(input())
# dgt_2 = int(input())
# Addition part
def addition():
    print('*******************************************************')
    print("Welcome to the addition part!!!")
    print()
    dgt_1 = int(input("Enter the first digit: \n"))
    dgt_2 = int(input("Enter the second digit: \n"))
    
    total = dgt_1 + dgt_2
    print("The result of your addition is: ", total)
    print("Happy to serve you :)")

# soustraction part
def soustraction():
    print('*******************************************************')
    print("Welcome to the soustraction part!!!")
    print()
    dgt_1 = int(input("Enter the first digit: \n"))
    dgt_2 = int(input("Enter the second digit: \n"))
    total = dgt_1 - dgt_2
    print("The result of your substraction is: ", total)
    print("Happy to serve you :)")


# multiplication part
def multiplication():
    print('*******************************************************')
    print("Welcome to the multiplication part!!!")
    print()
    dgt_1 = int(input("Enter the first digit: \n"))
    dgt_2 = int(input("Enter the second digit: \n"))
    total = dgt_1 * dgt_2
    print("The result of your multiplication is: ", total)
    print("Happy to serve you :)")

# Division part
def division():
    print('*******************************************************')
    print("Welcome to the division part!!!")
    print()
    dgt_1 = int(input("Enter the first digit: \n"))
    dgt_2 = int(input("Enter the second digit: \n"))
    total = dgt_1 / dgt_2
    print("The result of your division is: ", total)
    print("Happy to serve you :)")

# modulo part
def modulo():
    print('*******************************************************')
    print("Welcome to the modulo part!!!")
    print()
    dgt_1 = int(input("Enter the first digit: \n"))
    dgt_2 = int(input("Enter the second digit: \n"))
    total = dgt_1 % dgt_2
    print("The result of your modulo is: ", total)
    print("Happy to serve you :)")
    
    
# Power part
def power():
    print('*******************************************************')
    print("Welcome to the power part!!!")
    print()
    dgt_1 = int(input("Enter the first digit: \n"))
    dgt_2 = int(input("Enter the second digit: \n"))
    total = dgt_1 ** dgt_2
    print("The result of your power is: ", total)
    print("Happy to serve you :)")

# **************************************************************************************************************************************
# **************************************************************************************************************************************



# **************************************************************************************************************************************
# **************************************************************************************************************************************

print('*******************************************************')
print('*******************************************************')
print('Welcome to our professionnal Calculator')
print()
# **************************************************************************************************************************************
# **************************************************************************************************************************************

# **************************************************************************************************************************************
# **************************************************************************************************************************************

possibleChoice = ['a', 's', 'm','d', 'r', 'p']


# **************************************************************************************************************************************
# **************************************************************************************************************************************

print("press :a: for addition")
print("press :s: for soustraction")
print("press :m: for multiplication")
print("press :d: for division")
print("press :r: for modulo")
print("press :p: for power")
print()
ans = input("What is your Choice: ")


# **************************************************************************************************************************************
# **************************************************************************************************************************************

while ans not in possibleChoice:

    print("*************************************************")
    print("*************************************************")
    print("press :a: for addition")
    print("press :s: for soustraction")
    print("press :m: for multiplication")
    print("press :d: for division")
    print("press :r: for modulo")
    print("press :p: for power")
    print()
    print('You press the wrong key, try again or')
    print("\'x: for power to quit the calcul")
    print()
    ans = input(" So what is your new Choice: ")
    if ans == 'x' or ans == "X":
        print('You just break the calcul successfully')
    

# **************************************************************************************************************************************
# **************************************************************************************************************************************

if ans == 'a':
    addition()

elif ans == 's':
    soustraction()

elif ans == 'm':
    multiplication()

elif ans == 'd':
    division()

elif ans == 'r':
    modulo()

elif ans == 'p':
    power()

# **************************************************************************************************************************************
# **************************************************************************************************************************************
