import random

#Split the names and add to a list that are given as the input
names_input = input("Enter the names of your friends: \n")
names = names_input.split(", ")
print(names)

#get a random integer
print(len(names)-1)
random_number = random.randint(0,len(names)-1)
print(f"The payement should made by: {names[random_number]}\n")

#this can replace random.choice function
person_pay = random.choice(names)
print(f"pay by: {person_pay}\n")

for i in range(3):
    print(random.choice(names))
