"""
Course CS2302 MW 1:30-2:50pm
Instructor:Fuentes, Olac
Tovar, Brianna
Date of last modification: 4/29/2019
7th Lab
This lab is over creating our own maze, and prompting the user to remove walls.
using algorithms
"""

import matplotlib.pyplot as plt
import numpy as np
import random

def DisjointSetForest(size):
    return np.zeros(size,dtype=np.int)-1      
  
def dsfToSetList(S):
    #Returns aa list containing the sets encoded in S
    sets = [ [] for i in range(len(S)) ]
    for i in range(len(S)):
        sets[find(S,i)].append(i)
    sets = [x for x in sets if x != []]
    return sets

def find(S,i):
    # Returns root of tree that i belongs to
    if S[i]<0:
        return i
    return find(S,S[i])

def find_c(S,i): #Find with path compression 
    if S[i]<0: 
        return i
    r = find_c(S,S[i]) 
    S[i] = r 
    return r
    
def union(S,i,j): #removing walls
    # Joins i's tree and j's tree, if they are different
    ri = find(S,i) 
    rj = find(S,j)
    if ri!=rj:
        S[rj] = ri

def union_c(S,i,j): #removing walls
    # Joins i's tree and j's tree, if they are different
    # Uses path compression
    ri = find_c(S,i) 
    rj = find_c(S,j)
    if ri!=rj:
        S[rj] = ri
         
def union_by_size(S,i,j): #removing walls
    # if i is a root, S[i] = -number of elements in tree (set)
    # Makes root of smaller tree point to root of larger tree 
    # Uses path compression
    ri = find_c(S,i) 
    rj = find_c(S,j)
    if ri!=rj:
        if S[ri]>S[rj]: # j's tree is larger
            S[rj] += S[ri]
            S[ri] = rj
        else:
            S[ri] += S[rj]
            S[rj] = ri

def NumSets(S):
    count =0
    for i in range(len(S)):
        if S[i]<0:
            count += 1
    return count


####################################################
#displaying the maze
def draw_maze(walls,maze_rows,maze_cols,cell_nums=False):
    fig, ax = plt.subplots()
    for w in walls:
        if w[1]-w[0] ==1: #vertical wall
            x0 = (w[1]%maze_cols)
            x1 = x0
            y0 = (w[1]//maze_cols)
            y1 = y0+1
        else:#horizontal wall
            x0 = (w[0]%maze_cols)
            x1 = x0+1
            y0 = (w[1]//maze_cols)
            y1 = y0  
        ax.plot([x0,x1],[y0,y1],linewidth=1,color='k')
    sx = maze_cols
    sy = maze_rows
    ax.plot([0,0,sx,sx,0],[0,sy,sy,0,0],linewidth=2,color='k')
    if cell_nums:
        for r in range(maze_rows):
            for c in range(maze_cols):
                cell = c + r*maze_cols   
                ax.text((c+.5),(r+.5), str(cell), size=10,
                        ha="center", va="center")
    ax.axis('off') 
    ax.set_aspect(1.0)

def wall_list(maze_rows, maze_cols):
    # Creates a list with all the walls in the maze
    w =[]
    for r in range(maze_rows):
        for c in range(maze_cols):
            cell = c + r*maze_cols
            if c!=maze_cols-1:
                w.append([cell,cell+1])
            if r!=maze_rows-1:
                w.append([cell,cell+maze_cols])
    return w

plt.close("all") 
maze_rows = 5
maze_cols = 10

walls = wall_list(maze_rows,maze_cols)
#using dsf to create the maze
S = DisjointSetForest(maze_rows*maze_cols)
#drawing numbered maze
draw_maze(walls,maze_rows,maze_cols,cell_nums=True)

#############################
num_cells=maze_rows*maze_cols
print("There are, ",num_cells,"cells in this maze.")
num_remove=int(input("How many walls do you want to remove?"))

#union standard
#removing amount of walls user inputs
for i in range(num_remove): #removing amount of walls user inputs
    r=random.randint(0,len(walls)-1)
    union(S, walls[r][0], walls[r][1])
    walls.pop(r)
    num_remove=num_remove-1
    
draw_maze(walls,maze_rows,maze_cols)
print("Union Standard")
#union with compression
for i in range(num_remove): #removing amount of walls user inputs
    r=random.randint(0,len(walls)-1) #finding random number to use to remove wall
    union_c(S, walls[r][0], walls[r][1])
    walls.pop(r)
    num_remove=num_remove-1
    
draw_maze(walls,maze_rows,maze_cols)
print("Union with Compression")

#1, checking if created maze is unique
def check(m,n): #check, m=num_remove, n=number of cells
    if m>n-1:
        print("A path from source to destination is not guaranteed to exist")
    if m==n-1:
        print("The is a unique path from source to destination")
    if m<n-1:
        print("There is at least one path from source to destination")

check(num_remove,num_cells)

#2, Adj list of my maze
def build_Adj(r,c,w): #not correct
    list=[len(w)]
    for i in range(r):
        for j in range(c):
            list.append(i,j)
            
print("Adjacency list: ",build_Adj)#not fixed

#3, Searches
def breadth():
    #needs adj list to use
    return

def depth():
    #needs adj list to use
    return

def depth_r():
    #needs adj list to use
    return

#4, paths
def path():
    #not finished
    return