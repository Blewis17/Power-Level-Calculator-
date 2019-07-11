print(" Hi, welcome to the power reader 10,000 the newest in its design. I make no mistakes. Now lets get started. This canculator will read the strenth of your power and your spiritual power then it will add up to a total. ")






import random 


names = input(" What is your name? ")
print(names)

print("Hello, I'm going to read you your level now.")
Level = input("What do you think your strength level is on this scale of 1 - 1000000?") 

Y = random.randint(1, 1000000)
print("Well, " + names + " your strength level is actually " + str(Y))
T = random.randint(1, 1000000)
level = input("what do you think your spiritual level is on a scale of 1 - 1000000?")
print("Well, " + names + " your spiritual level is actually " + str(T))

def add (Y, T):
    return Y + T
print(add(Y, T))
# def tot_overall():
total= input("Now that you know your power levels, do you want to know your overal power level?")

# def add (Y, T):
#     return Y + T
    
if total.lower() == "no":
    print("Bye see you next time!")
elif total.lower() == "yes":
    print("Your total power level is " + str(add(Y,T)))
else:
    print("Sorry pick between yes or no")
# print(total)  












# def add(x, y):
#   return x + y






































































































































































