grid = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
turn = 1

def fill_cell(cell_no):
    global turn
    grid[int((cell_no-1)/3)][(cell_no-1)%3] = "X" if turn == 1 else "O"
    turn =  2 if turn == 1 else 1  

def user_input():
    print(f"Player {turn}'s turn")
    cell_no = input("Please enter the cell in which you want to enter the symbol from 1 to 9")
    while cell_no.isdigit == False or int(cell_no)<1  or int(cell_no)>9:
        input("Please enter a digit between 1 and 9 only no other character allowed")
    cell_no = int(cell_no)
    while grid[int((cell_no-1)/3)][(cell_no-1)%3] != " ":
        print(grid[int((cell_no-1)/3)][(cell_no-1)%3])
        cell_no = input("Please enter correct cell the cell you requested for earlier was already taken")
    fill_cell(cell_no)

def display_grid():
    for row in grid:
        for cell in row:
            print(cell, end=" ")
        print("\n")

def decide_winner():
    # All the possibilities for player 2 to win 
    if any(all(cell == 'X' for cell in row) for row in grid):
        return 1
    for i in range(3):
        if all(row[i]=="X" for row in grid):
            return 1
    if grid[0][0]==grid[1][1]==grid[2][2]=="X" or grid[0][2]==grid[1][1]==grid[2][0]=="X":
        return 1
    # All the possibilities for player 2 to win 
    if any(all(cell == 'O' for cell in row) for row in grid):
        return 2
    for i in range(3):
        if all(row[i]=="O" for row in grid):
            return 2
    if grid[0][0]==grid[1][1]==grid[2][2]=="O" or grid[0][2]==grid[1][1]==grid[2][0]=="O":
        return 2
    return 0


def start_game():
    while any(" " in row for row in grid):
        display_grid()
        user_input()
    display_grid()
    winner =  decide_winner()
    if winner == 0:
        print("Match is drawn noone wins")
    if winner == 1:
        print("Player 1 congratulations you won")
    if winner == 2:
        print("Player 2 congratulations you won")

start_game()