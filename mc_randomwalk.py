import numpy
import numpy.random
import numpy.linalg

# Establish random number generation
rng = numpy.random.default_rng()

# Read the data and set variables
with open("mc_randomwalk_input.txt") as file:
    d = int(file.readline())
    k = int(file.readline()) 
    N = int(file.readline())

# Monte Carlo method
total = 0
for i in range(N):
    position = numpy.zeros((d,))
    for step in range(k):
        choosen_coord = rng.integers(len(position))
        update = rng.choice([-1,1],p=[0.5,0.5])
        position[choosen_coord] += update
    
    total += numpy.linalg.norm(position)

print(total/N)