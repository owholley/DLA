import matplotlib.pyplot as plt
import numpy as np
from particle import Particle


#------------------------------------------------------------------------------
# Algorithm

# Prompt the user to provide the axis length and the number of particles
while True:
    try:
        axis_length = int(input("Please enter the desired length of the axes: "))
        break
    except ValueError:
        print("\nOops, that was not a valid integer, please try again.\n")

while True:
    try:
        number_particles = int(input("Please enter the desired number of particles: "))
        break
    except ValueError:
        print("\nOops, that was not a valid integer, please try again.\n")



# set the seed to be [0, -axis_length] a.k.a the middle of the bottom axis
stuck_list = [
    [0 , 0],
]

# generate 'number_particles' particles
particles = [
    Particle(axis_length, stuck_list) for i in range(0, number_particles, 1)
]


for particle in particles:
    particle.walk_particle()

print(stuck_list)
print(len(stuck_list))


#------------------------------------------------------------------------------
# Plot

axis = np.arange(-axis_length, axis_length, 1) # Set the axis length and the seed position

for element in stuck_list:
    plt.plot(element[0], element[1], 'ro')

plt.plot(stuck_list[0][0], stuck_list[0][1], 'ko')                                     # Plot functions



plt.xticks(np.arange(min(axis), max(axis)+1, 1), [])
plt.yticks(np.arange(min(axis), max(axis)+1, 1), [])
plt.grid()

# plt.savefig('dla_middle_seed.png')
plt.show()
