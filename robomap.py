# this is the game map, as a 2d list
# 0 - empty
# 1 - wall
# 2 - robot
# 3 - 
from os import system
gamemap = [
[0,0,0,0,0,0,0,0,0,0], #0
[1,1,1,1,1,0,0,0,0,0], #1
[0,0,0,0,0,0,0,0,0,0], #2
[1,0,0,0,0,0,0,0,0,1], #3
[1,0,0,0,1,1,1,0,0,1], #4
[0,0,0,0,0,1,0,0,0,1], #5
[1,1,1,1,0,1,0,0,0,0], #6
[0,0,0,0,0,1,0,0,0,0], #7
[0,0,0,0,0,1,0,0,0,1], #8
[0,0,0,0,0,0,0,0,0,1], #9
#0 1 2 3 4 5 6 7 8 9 
]

def robot_in_pos(which):
    print (f"input {which} : ", end = "")
    return int(input())
c=robot_in_pos("column")
r=robot_in_pos("row")

bc, br=4, 2


def print_map(m):
    for rr in range(10):
        print ()
        for rc in range (10):
            m[br][bc]=3
            if m[rr][rc]==0:
                print (" .", end="")
            elif r==br and c==bc and m[rr][rc]!=1:
                print (" !", end="")
            elif m[rr][rc]==3:
                print (" x", end="")
            elif m[rr][rc]==1:
                print (" #", end="")
            else:
                print (" R", end="")

def controls():
    while True:
        global c
        global r
        system("cls")
        print_map (gamemap)
        if bc==c and br==r:
            print ("\nCollapse")
            break
        elif bc-c<=2 and c-bc<=2 and br==r:
              print ("\ndanger")

        key=input("\n>>> ")
        if key == "x":
            break

        if c<=8 and key =="d" and gamemap[r][c+1]!=1:        
                gamemap[r][c]=0
                gamemap[r][c+1]=2
                c+=1                
        elif c>0 and key =="a" and gamemap[r][c-1]!=1:        
                gamemap[r][c]=0
                gamemap[r][c-1]=2
                c-=1
        elif r>0 and key =="w" and gamemap[r-1][c]!=1:        
                gamemap[r][c]=0
                gamemap[r-1][c]=2
                r-=1
        elif r<=8 and key =="s" and gamemap[r+1][c]!=1:        
                gamemap[r][c]=0
                gamemap[r+1][c]=2
                r+=1
    
