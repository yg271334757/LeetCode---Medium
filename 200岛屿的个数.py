class Solution:
    def numIslands(self, grid):  # DFS
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        def fd(grid,x,y,r,c):
            grid[x][y]='-1'
            if x>0 and grid[x-1][y]=='1':
                fd(grid,x-1,y,r,c)
            if x<r-1 and grid[x+1][y]=='1':
                fd(grid,x+1,y,r,c)
            if y>0 and grid[x][y-1]=='1':
                fd(grid,x,y-1,r,c)
            if y<c-1 and grid[x][y+1]=='1':
                fd(grid,x,y+1,r,c)
        r,c=len(grid),len(grid[0])
        count = 0
        for x in range(r):
            for y in range(c):
                if grid[x][y]=='1':
                    fd(grid,x,y,r,c)
                    count += 1
        return count
'''
from collections import deque
class Solution:
    def numIslands(self, grid): # BFS
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        if not grid:
            return count
        r = len(grid)
        c = len(grid[0])
        for i in range(r):
            for j in range(c):
                if grid[i][j] == '0':
                    continue
                count += 1
                dq = deque([(i, j)])
                while dq:
                    p, q = dq.popleft()
                    if p - 1 >= 0 and grid[p-1][q] == '1' and (p-1, q) not in dq:
                        dq.append((p-1, q))
                        grid[p-1][q] = '0'
                    if p + 1 < r and grid[p+1][q] == '1' and (p+1, q) not in dq:
                        dq.append((p+1, q))
                        grid[p+1][q] = '0'
                    if q - 1 >= 0 and grid[p][q-1] == '1' and (p, q-1) not in dq:
                        dq.append((p, q-1))
                        grid[p][q-1] = '0'
                    if q + 1 < c and grid[p][q+1] == '1' and (p, q+1) not in dq:
                        dq.append((p, q+1))
                        grid[p][q+1] = '0'
                    grid[p][q] = '0'
        return count
'''