# Test the DLA algorithm
import unittest
import matplotlib.pyplot as plt
import numpy as np

from particle import Particle

stuck_list = [
    [0, 0],
]
axis_length = 10


class TestInitialPosition(unittest.TestCase):
    
    def test_initial_position(self):
        """
        Test to determine if the iniital position of the particles is suffeciently
        far away from the seed particle.
        """
        particle = Particle(axis_length, stuck_list)
        particle.generate_initial_position()
        particle.print_particle_position()
        dist = np.linalg.norm([particle.get_particle_position(), stuck_list[0]])
        self.assertTrue(dist > axis_length/2), f'{dist}'
        
        

    

if __name__ == '__main__':
    unittest.main()
