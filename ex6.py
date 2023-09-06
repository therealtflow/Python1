row = int(input('Enter a row number from 1 to 5: '))
column = int(input('Enter a column number from 1 to 5: '))


grid = [[0 for x in range(5)] for y in range(5)]
grid[row - 1][column - 1] = 1
print(grid)