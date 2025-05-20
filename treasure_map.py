
row1 = ["0","0","0"]
row2 = ["0","0","0"]
row3 = ["0","0","0"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}\n")

print("Answer in syntax: column, row\n")

""" column = (input("what column do you want to put your X: \n"))
columnInt = int(column)-1
row = (input("what row do you want to put your X: \n"))
rowInt = int(row)-1 

answer = column+row
map[columnInt][rowInt] = "X"
print(map) """

position = input("Enter your postion: ")

column = int(position[0])-1
row = int(position[1])-1

map[column][row] = "X"
print(map)


