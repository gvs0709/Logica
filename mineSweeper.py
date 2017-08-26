import numpy as np

f=open("input.txt")

temp=[]

for line in f:
    vec=line
    data=int(vec)

    temp.append(data)

#print temp
f.close()

class Grid():
    m=temp[0] #Number of lines
    n=temp[1] #Number of columns
    x=temp[2] #Number of mines

    def gridSize(self): #Shows the grid size and the number of mines
        m=self.m
        n=self.n
        x=self.x

        print "Grid Size:", m, "x", n
        print "Mines:", x

    def setGrid(self): #Creates the grids and places mines
        m=self.m
        n=self.n
        x=self.x
        grid=np.zeros((m, n), int, 'C') #Grid that stores mines position
        grid2=np.zeros((m, n), int, 'C') #Grid shown to player

        for i in xrange(0, m): #Fills grid2 with -1 to indicate a position not opened
            for j in xrange(0, n):
                grid2[i, j]=-1

        np.random.seed()
        l=np.random.randint(m)
        c=np.random.randint(n)

        for i in xrange(0, x): #Randomly places mines on grid
            if grid[l, c]==1:
                while grid[l, c]==1:
                    l=np.random.randint(m)
                    c=np.random.randint(n)

                grid[l, c]=1

            else:
                grid[l, c]=1

        print grid
        #print grid2

def tao():
    grid=Grid()
    grid.gridSize()
    grid.setGrid()


tao=tao()
