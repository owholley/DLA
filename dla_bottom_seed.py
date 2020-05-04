import matplotlib.pyplot as plt
import numpy as np
from particle import Particle


#------------------------------------------------------------------------------
# Generate the particles and run them through the simulation
axis_length = int(input("Please enter the desired length of the axes: "))
number_particles = int(input("Please enter the desired number of particles: "))
seed =  round(axis_length / 2)

# set the seed to be [seed, 0]
stuck_list = [
    [seed, 0],
]

# generate 'number_particles' particles
particles = [
    Particle(axis_length, stuck_list) for i in range(0, number_particles, 1)
]


for particle in particles:
    if particle.walk_particle() :
        stuck_list.append([particle.x, particle.y],)

print(stuck_list)


#------------------------------------------------------------------------------
# Plot

axis = np.arange(0, axis_length, 1) # Set the axis length and the seed position

for element in stuck_list:
    plt.plot(element[0], element[1], 'ro')

plt.plot(seed, 0, 'ko')                                     # Plot functions

plt.xticks(np.arange(min(axis), max(axis)+1, 1), [])
plt.yticks(np.arange(min(axis), max(axis)+1, 1), [])
plt.grid()

plt.show()