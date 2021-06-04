import math
import numpy
import numpy.random
import numpy.linalg

# Establish random number generation
rng = numpy.random.default_rng()

# Read the data and set the coordinates and number of trials
with open("mc_unitball_input.txt") as file:
    point = [float(num) for num in file.readline().split(",")]
    N = int(file.readline())

# Monte carlo method
total = 0.0
for i in range(0,N):
    coords = [0]*len(point)
    distance = [0]*len(point)

    for j in range(0,len(point)):
        # Draw coordinates uniformly at random from a square containing the unit disk
        coords[j] = rng.uniform(point[j]-1.0,point[j]+1.0)
        distance[j] = abs(point[j]-coords[j])
    
    squared = [number ** 2 for number in distance]
    sum_squares = sum(squared)
        
    # Ensure that the point lies inside the circle and redraw until it does
    while math.sqrt((sum_squares)) > 1:
        for k in range(0,len(point)):
            coords[k] = rng.uniform(point[k]-1.0,point[k]+1.0)
            distance[k] = abs(point[k]-coords[k])
        
        squared = [number ** 2 for number in distance]
        sum_squares = sum(squared)
            
    # Add distance between points to running total
    total += numpy.linalg.norm(coords)

print(total/N)