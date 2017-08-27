import numpy as np

# Ensure Python 2 and 3 Compatibility
try:
    input = raw_input
    range = xrange
except NameError:
    pass

'''f=open("input.txt")

temp=[]

for line in f:
    vec=line
    data=int(vec)

    temp.append(data)

#print(temp)
f.close()'''

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
        print("Mines:", x''')

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
        #print(grid)
        print(grid2)

    def mineScan(self):
        m=self.m
        n=self.n
        grid=self.grid
        grid2=self.grid2

        in1=input("Select line to open:")
        l=int(in1)

        '''if l<0 or l>m: #Checks if l is bigger than m
            while'''

        in2=input("Select column to open:")
        c=int(in2)

        '''if c<n: #Checks if c is smaller than n
            pass'''

        if grid[l, c]==1:
            grid2[l, c]=9 #Nine indicates a mine, because its an impossible value for counter
            self.grid2[l, c]=grid2[l, c]

            print("BOOM!")
            print("Game Over")
            print(grid2)
            return -1

        else:
            counter=0
            counter=grid[(l-1), (c-1)]+grid[(l-1), c]+grid[(l-1), (c+1)]+grid[l, (c-1)]+grid[l, (c+1)]+grid[(l+1), (c-1)]+grid[(l+1), c]+grid[(l+1), (c+1)]
            grid2[l, c]=counter
            self.grid2[l, c]=grid2[l, c]

            print(grid2)
            return counter

    '''def run(self): #Check later!!!
        pass'''

def tao(): #Under work!!!
    in1=input("Enter number of lines:")
    in2=input("Enter number of columns:")
    in3=input("Enter number of mines:")

    m=int(in1)
    n=int(in2)
    x=int(in3)

    grid=Grid(m, n, x)
    grid.setGrid()

tao=tao()