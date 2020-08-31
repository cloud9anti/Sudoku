#Take an object based on the sudoku puzzle and evaluate whether the puzzle is valid or invalid.
#If the function returns true, the puzzle is valid and does not have any errors. If the function returns False
#at any point, print the reason why the puzzle is invalid.
#In the future, I plan to test beyond 16x16 puzzles and play on fullscreen using pygame.

def sudokuChecker(grid, size):
    #set the size of the sudoku puzzle
    gridSize = size*3
    #loop through the rows and columns
    for i in range(0, gridSize):
        row = []
        column = []
        block = []
        for j in range(0, gridSize):
            #if the column contains the same number, the puzzle in invalid.
            if grid[j][i] in column and grid[j][i]!="0":
                print("There are too many numbers in one of the 9 columns!")
                return False
            column.append(grid[j][i])
            
            #if the row contains the same number, the puzzle in invalid.
            if grid[i][j] in row and grid[i][j]!="0":
                print("There are too many numbers in one of the 9 rows!")
                return False
            row.append(grid[i][j])

            x= (size * (i // size)) + j // size
            y = (size * (i % size)) + j % size
                
            #If the block contains the same number, the puzzle is invalid.
            if grid[x][y] in block and grid[x][y]!="0":
                print(grid[x][y])
                print("There are too many numbers in one of the 9 blocks!")
                return False
            block.append(grid[x][y])
    return True

#Validate the easy Puzzle
 
with open("easy.txt") as textFile:
    easy = [line.split() for line in textFile]
print("Easy Puzzle: ")
print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
    for row in easy]))

if sudokuChecker(easy, 3) == 1:
    print("This puzzle is valid.")
    print("\n")
else:
    print("This puzzle is invalid.")

#Validate the medium Puzzle

with open("medium.txt") as textFile:
    medium = [line.split() for line in textFile]
print("Medium Puzzle: ")
print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
    for row in medium]))

if sudokuChecker(medium, 3) == 1:
    print("This puzzle is valid.")
    print("\n")
else:
    print("This puzzle is invalid.")
    
#Validate the expert Puzzle

with open("expert.txt") as textFile:
    expert = [line.split() for line in textFile]
print("Expert Puzzle: ")
print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
    for row in expert]))

if sudokuChecker(expert, 3) == 1:
    print("This puzzle is valid.")
    print("\n")
else:
    print("This puzzle is invalid.")    

#Validate the 12x12 Puzzle

with open("12x12.txt") as textFile:
    twelveByTwelve = [line.split() for line in textFile]
print("12x12 Puzzle: ")
print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
    for row in twelveByTwelve]))

if sudokuChecker(twelveByTwelve, 4) == 1:
    print("This puzzle is valid.")
    print("\n")
else:
    print("This puzzle is invalid.") 
  