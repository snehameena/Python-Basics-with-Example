## Solvin dist between 2 points formula:
import math

def distance_cal(x1,x2,y1,y2):
    dx = int( x2 - x1 )**2
    dy = int( y2 - y1 )**2
    dist = math.sqrt(dx+dy)
    return dist

## Main function
x1 = 3
x2 = 10
y1 = 2
y2 = 20
print("The distance is:",distance_cal(x1,x2,y1,y2))