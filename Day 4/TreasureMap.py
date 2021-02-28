#In this exercise we'll practice the use of indexes. We have to think as users, so for the position 0,0 the user is going to use 1,1, for is the fisrt position in the first row, and the user doesn't know if that is 0,0 in therms of programming
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

print("Where do you want to put the treasure? ")
print("Please, specify first the column and then the row.")
position = input("Write both numbers separated by a comma: ")
column_row_position = position.split(",")

map[int(column_row_position[1]) -1 ][int(column_row_position[0]) -1] = 'x' #Remember: first we select the list and then the item!

print(f"{row1}\n{row2}\n{row3}")
