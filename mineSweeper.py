import numpy as np
from itertools import chain, combinations
from os import linesep

#Ensure Python 2 and 3 Compatibility
try:
    input = raw_input
    range = xrange

except NameError:
    pass

class Grid():
    def __init__(self, m, n, x): #Sets the grid size (m, n) and the number number of mines
        self.m=m #Number of lines
        self.n=n #Number of columns
        self.x=x #Number of mines
        self.grid=[]
        self.grid2=[]

    '''def getSize(self): #Returns number of rows, columns and mines
        m=self.m
        n=self.n
        x=self.x

        return (m, n, x)

    def gridSize(self): #Shows the grid size and the number of mines
        m=self.m
        n=self.n
        x=self.x

        print("Grid Size:", m, "x", n)
        print("Mines:", x)'''

    def setGrid(self): #Creates the grids and places mines
        m=self.m
        n=self.n
        x=self.x
        grid=np.zeros((m, n), int, 'C') #Grid that stores mines position
        grid2=np.zeros((m, n), int, 'C') #Grid shown to player

        for i in range(0, m): #Fills grid2 with -1 to indicate a position not opened
            for j in range(0, n):
                grid2[i, j]=-1

        np.random.seed()
        l=np.random.randint(m)
        c=np.random.randint(n)

        for i in range(0, x): #Randomly places mines on grid
            if grid[l, c]==1:
                while grid[l, c]==1:
                    l=np.random.randint(m)
                    c=np.random.randint(n)

                grid[l, c]=1

            else:
                grid[l, c]=1

        self.grid=grid
        self.grid2=grid2
        print(grid)
        #print(grid2)

    def mineScan(self):
        m=self.m
        n=self.n
        grid=self.grid
        grid2=self.grid2

        l=int(input("Select line to open:"))

        while l<0 or l>(m-1): #Checks if l is smaller or bigger than m
            message1="This line is out of the grid. Lines goes from 0 to {}".format(m-1)
            print(message1)
            l=int(input("Select line to open:"))

        c=int(input("Select column to open:"))

        while c<0 or c>(n-1): #Checks if c is smaller or bigger than n
            message2="This column is out of grid. Columns goes from 0 to {}".format(n-1)
            print(message2)
            c=int(input("Select column to open:"))

        if grid[l, c]==1:
            grid2[l, c]=9 #Nine indicates a mine, because its an impossible value for counter
            self.grid2[l, c]=grid2[l, c]

            print("BOOM!")
            print("Game Over")
            print(grid2)
            return -1

        else: #Processes not mined titles and the border conditions
            counter=0

            if l==0 and c!=0 and c!=(n-1):
                counter=grid[l, (c-1)]+grid[l, (c+1)]+grid[(l+1), (c-1)]+grid[(l+1), c]+grid[(l+1), (c+1)]

            elif c==0 and l!=0 and l!=(m-1):
                counter=grid[(l-1), c]+grid[(l-1), (c+1)]+grid[l, (c+1)]+grid[(l+1), c]+grid[(l+1), (c+1)]

            elif l==0 and c==0:
                counter=grid[l, (c+1)]+grid[(l+1), c]+grid[(l+1), (c+1)]

            elif l==0 and c==(n-1):
                counter=grid[l, (c-1)]+grid[(l+1), (c-1)]+grid[(l+1), c]

            elif l==(m-1) and c!=0 and c!=(n-1):
                counter=grid[(l-1), (c-1)]+grid[(l-1), c]+grid[(l-1), (c+1)]+grid[l, (c-1)]+grid[l, (c+1)]

            elif c==(n-1) and l!=0 and l!=(m-1):
                counter=grid[(l-1), (c-1)]+grid[(l-1), c]+grid[l, (c-1)]+grid[(l+1), (c-1)]+grid[(l+1), c]

            elif l==(m-1) and c==0:
                counter=grid[(l-1), c]+grid[(l-1), (c+1)]+grid[l, (c+1)]

            elif l==(m-1) and c==(n-1):
                counter=grid[(l-1), (c-1)]+grid[(l-1), c]+grid[l, (c-1)]

            else:
                counter=grid[(l-1), (c-1)]+grid[(l-1), c]+grid[(l-1), (c+1)]+grid[l, (c-1)]+grid[l, (c+1)]+grid[(l+1), (c-1)]+grid[(l+1), c]+grid[(l+1), (c+1)]

            grid2[l, c]=counter
            self.grid2[l, c]=grid2[l, c]

            print(grid2)
            return counter

def tau(m, n, x):
    prop=[] #List of all possible mined tiles

    for i in range(0, m): #Generate all possible mined tiles
        for j in range(0, n):
            tile=(i, j) #Create tile as tuple
            prop.append(tile)

    possible_grids=list(combinations(prop, x)) #Generate all possible grids (tau interpretations)

    return possible_grids

def generate_grid_conditional(tile_line, tile_column, possible_grids):
    specified_tile=(tile_line, tile_column)
    conditional_grids=[]

    for grid in possible_grids: #Select Grids that do not contain specified Tile
        if specified_tile not in grid:
            conditional_grids.append(grid)
    
    return conditional_grids

def print_grid(grids):
    for grid in grids:
        print(grid)

def user_interface():
    print("---------------------------")
    print("    Logic - Minesweeper    ")
    print("---------------------------\n")

    # -------- Part A --------

    #Read Grid Size
    print("Grid Information")
    m=int(input("Enter the number of lines: "))
    n=int(input("Enter the numbers of columns: "))
    x=int(input("Enter the numbers of mines: "))

    possible_grids=tau(m, n, x) #Generate all Possible Grids (Tau Intepretations)

    print("\nPossible Grids: ")
    print_grid(possible_grids) #Display Possible Grids

    # -------- Part B --------

    g=Grid(m, n, x)
    g.setGrid()

    np.random.seed()
    tile_line=np.random.randint(m) #Chooses a random grid line
    tile_column=np.random.randint(n) #Chooses a random grid column

    if g.grid[tile_line, tile_column]==1: #Select tile that does not contain a mine
        while g.grid[tile_line, tile_column]==1:
            tile_line=np.random.randint(m)
            tile_column=np.random.randint(n)

    '''print("\nPlease enter a tile that does not contain a mine.")
    tile_line = int(input("Tile line: "))
    tile_column = int(input("Tile column: "))'''

    conditional_grids=generate_grid_conditional(tile_line, tile_column, possible_grids) #Generate All Possible Grids whose specified tile does not have a mine

    message_2="\nPossible grids without mine at tile {}x{}:".format(tile_line, tile_column)
    print(message_2)
    print_grid(conditional_grids) #Print Possible Grids without specified tile

    # -------- Part C --------

    #letra c aqui!!!


#tau=tau()
#g=Grid(3, 3, 2)
#g.setGrid()
#g.mineScan()
user_interface()
