import numpy as np
import matplotlib.pyplot as plt

class Particle:

    def __init__(self, axis_length, stuck_list):
        self.axis_length = axis_length
        self.stuck_list = stuck_list 
        self.steps = 0

    def generate_initial_position(self):
        ''' start at a random distant position from the seed '''
        self.x = np.random.randint(-self.axis_length/2, self.axis_length)
        self.y = np.random.randint(-self.axis_length/2, self.axis_length)

    def get_particle_position(self):
        return [self.x, self.y]

    def print_particle_position(self):
        print(f'Particle Position: [{self.x}, {self.y}] \n')

    def take_step(self):
        ''' TODO add in a dictionary/vector containing the direction of movement ''' 
        # direction = 2
        direction = np.random.randint(0,3)      # Randomly generate a number 0, 1, 2, or 3 to indicate movement up, right,
                                                # down, or left, respectively
        if direction == 0:          # up
            self.y += 1
        elif direction == 1:        # right
            self.x += 1
        elif direction == 2:        # down
            self.y -= 1
        else:                       # left
            self.x -= 1
        
        self.steps += 1

    def is_frozen(self):
        ''' docstring '''
        # stuck
        if [self.x, self.y-1] in self.stuck_list or \
           [self.x, self.y+1] in self.stuck_list or \
           [self.x-1, self.y] in self.stuck_list or \
           [self.x+1, self.y] in self.stuck_list:
            print(f'STUCK!!!! Particle stuck after {self.steps} steps')
            self.print_particle_position()
            return True
        # free
        else:
            return False

    def at_boundary(self):
        ''' checks to see if the particle is at the boundary; if the particle is at the boundary, the particle is flipped to the opposite side'''
        # at boundary
        if abs(self.y) > self.axis_length or abs(self.x) > self.axis_length:
            print(f'Whoops!! Particle left the lattice after {self.steps} steps!')
            return True
        else:

            return False

    def add_to_stucklist(self):
        self.stuck_list.append([self.x, self.y])

    def walk_particle(self):
        ''' docstring '''
        while self.is_frozen() is False and self.at_boundary() is False:
            self.take_step()
            if self.is_frozen() is True:
                self.add_to_stucklist()
        


