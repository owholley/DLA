import numpy as np
import matplotlib.pyplot as plt

class Particle: #(Aggregate):

    def __init__(self, axis_length, stuck_list):
        # Aggregate.__init__(self, axis_length, number_particles)
        self.axis_length = axis_length
        self.stuck_list = stuck_list
        self.seed = round(axis_length / 2)
        self.x = np.random.randint(0, self.axis_length)
        self.y = axis_length 
        self.steps = 0

    def displayParticlePosition(self):
        print(f'Particle Position: [{self.x}, {self.y}] \n')

    def take_step(self):
        ''' docstring ''' 
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
            self.displayParticlePosition()
            return True
        # free
        else:
            # print(f'Still free after {self.steps} step(s)')
            return False

    def at_boundary(self):
        ''' checks to see if the particle is at the boundary '''
        # at boundary
        if self.y < 0 or self.y > self.axis_length:
            print(f'Whoops!! Particle left the lattice after {self.steps} steps!')
            return True
        elif self.x < 0 or self.x > self.axis_length:                       # Axis is precariously hardcoded ATM ****
            print(self.y)
            print(f'Whoops!! Particle left the lattice after {self.steps} steps!')
            return True
        # not at boundary
        else:
            '''
            while self.is_frozen() is False:
                
            '''

            # print(f'Still on the lattice after {self.steps} steps!')
            return False

    def walk_particle(self):
        ''' docstring '''
        while self.is_frozen() is False and self.at_boundary() is False:
            self.take_step()
            if self.is_frozen() is True:
                return [self.x, self.y]
        


