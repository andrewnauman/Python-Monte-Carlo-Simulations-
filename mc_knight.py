import numpy
import numpy.random

rng = numpy.random.default_rng()

valid_moves = [numpy.array((i,j)) for i in (-2,-1,1,2) \
                for j in (-2,-1,1,2) if abs(i) != abs(j)]
def is_valid(position, M):
    if min(position) >= 0 and max(position) < M:
        return True
    else:
        return False

# Read the data
with open("mc_knight_input.txt") as file:
    M = int(file.readline())
    N = int(file.readline()) 

# Monte Carlo method
total = 0
for i in range(N):
    position = numpy.array([0,0])
    moves = 0
    while True:
        position_update = rng.integers(8)
        position = numpy.add(valid_moves[position_update],position)
        if is_valid(position, M) == True:
            moves +=1
        else:
            while is_valid(position, M) == False:
                position = numpy.subtract(position,valid_moves[position_update])
                position_update = rng.integers(8)
                position = numpy.add(valid_moves[position_update],position)
            moves += 1
        if position[0] == 0 and position[1] == 0:
            break
    total += moves
print(total/N)