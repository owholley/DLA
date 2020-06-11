import numpy as np
import matplotlib.pyplot as plt

class Particle:

    def __init__(self, axis_length, stuck_list):
        self.axis_length = axis_length
        self.stuck_list = stuck_list 
        self.steps = 0
        self.on_lattice = True
        self.frozen = False
        # The particle generation is left over from starting off thinking of
        #  the seed on the bottom of the lattice with application in terms of
        #  modeling frost formation on an existing snowpack.
        self.x = np.random.randint(-self.axis_length, self.axis_length)
        self.y = np.random.randint(-self.axis_length, self.axis_length)
        
    def get_particle_position(self):
        return [self.x, self.y]

    def print_particle_position(self):
        return(f'Particle Position: [{self.x}, {self.y}] \n')

    def pick_direction(self):
        direction = np.random.randint(0,4)
        return direction

    def take_step(self, direction):
        '''
        TODO add in a dictionary/vector containing the direction of movement
        ''' 
        # direction = 2
        if direction == 0:          # UP
            self.y += 1
        elif direction == 1:        # DOWN
            self.y -= 1
        elif direction == 2:        # LEFT
            self.x -= 1
        else:                       # RIGHT
            self.x += 1
        
        self.steps += 1
    
    def add_to_stuck_list(self):
        self.stuck_list.append([self.x, self.y])

    def is_frozen(self):
        ''' docstring '''
        # stuck_position = [
        #     [self.x+1, self.y],
        #     [self.x-1, self.y],
        #     [self.x, self.y+1],
        #     [self.x, self.y-1]
        # ]
        # if self.position in stuck_position:
        #     self.frozen = True
        #     self.print_particle_position()
        #     print(f'STUCK!!!! Particle stuck after {self.steps} steps.')
        if [self.x, self.y-1] in self.stuck_list or \
           [self.x, self.y+1] in self.stuck_list or \
           [self.x-1, self.y] in self.stuck_list or \
           [self.x+1, self.y] in self.stuck_list:
            print(f'STUCK!!!! Particle stuck after {self.steps} steps')
            self.print_particle_position()
            self.frozen = True
            self.add_to_stuck_list()

    def at_boundary(self):
        '''
        Checks to see if the particle is at the boundary; if the particle 
        touches the boundary, the particle exits the lattice. 
        '''
        if abs(self.y) > self.axis_length-1 or abs(self.x) > self.axis_length-1:
            self.on_lattice = False

    def walk_particle(self):
        '''
        While the particle is on the lattice and is not frozen to the 
        cluster 
        '''
        while self.on_lattice is True and self.frozen is False:
            self.take_step(self.pick_direction())
            self.at_boundary()
            self.is_frozen()      


