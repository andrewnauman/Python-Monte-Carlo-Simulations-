# Python-Monte-Carlo-Simulations-
3 Examples of Monte Carlo Simulations in Python

mc_unitball.py : Uses the Monte Carlo method to determine experimentally the expected distance of a randomly selected point in the unit ball in Rd from a given point x ∈ Rd. Simulation draws N points from the unit disk, each independently and uniformly at random. For each point, it computes the distance of the point to x. The average of the distances of the selected points to x is an approximation of the expected distance of a randomly selected point in the unit disk to x. Sample input file has output ~0.6654572119185038.

mc_randomwalk.py : Simulate a random walk on a d-dimensional integer lattice Zd. (A point in Zd can be regarded as a vector with d components, all of which are integers.) A particle will walk along the lattice in which the particle starts at the origin, for each step, one of the d possible coordinate directions is selected uniformly at random, and the particle then moves one step forward or backward in that coordinate direction with equal probability. Sample input file has output ~7.95976.

mc_knight.py : A knight is positioned in the lower left corner of an M × M chess board. The knight is moved around the board using valid moves, with each move selected uniformly at random from the set of moves available to the knight. This program calculates the expected number of moves until the knight returns to the lower left corner of the board. Sample input file has output ~24.
