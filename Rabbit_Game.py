row1= ['🌿','🌿','🌿']
row2= ['🌿','🌿','🌿']
row3= ['🌿','🌿','🌿']
print(f"""Welcome to place the rabbit game🐇
{row1}
{row2}
{row3}
Where should the rabbit go?🐇
Enter the position to place the rabbit""")
row = int(input("Enter the row = "))
column = int(input("Enter the column = "))
while True:
    if row not in [1, 2, 3] or column not in [1, 2, 3]:
        print("Invalid input, please enter a number 1 , 2 or 3 for both row and column")
        row = int(input("Enter the row = "))
        column = int(input("Enter the column = "))
    else:
        break 
if row == 1:
    row1[column-1] = '🐇'
elif row == 2:
    row2[column-1] = '🐇'
elif row == 3:
    row3[column-1] = '🐇'
print(f"""Success...
{row1}
{row2}
{row3}""")