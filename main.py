
from robomap import *
if gamemap[r][c]!=1:
    gamemap[r][c]=2
    controls()
else:
    print ("Coordinates the same as a wall. \nChoose other initial position")
