import random

""" random_integer =  random.randint(1, 100)
print(f"Your number is {random_integer}")

randoem_float = round((random.random() *6), 3)
print(f"\nYour number: {randoem_float}") """

randomNum = random.randint(0,1)

if randomNum ==0:
    print("Head")

elif randomNum == 1:
    print("Tail")

else:
    print("error")


#list data structure
fruits = ["apple", "orange", "Banana"]
fruits[2] = "pineapple"
print(fruits[2])    
print(fruits[-2])

fruits.append("car")
print(fruits)

fruits.extend(["van","bus"])
print(fruits)