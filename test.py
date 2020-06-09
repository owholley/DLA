# Test the DLA algorithm
# Going to write tests as if there is no program, then rebuild the algorithm
import unittest

from particle import Particle


class TestParticleGeneration(unittest.TestCase):
    
    def test_initial_position(self):
        """
        Test to determine if the iniital position of the particles is suffeciently
        far away from the seed particle (in the domain specified below).

        Domain: x,y in [-axis_length, -axis_length/2] U [axis_length/2, axis_length]

        Check: Distance from (x,y) to the seed particle at (0, 0) < axis_length/2
        """
        # particle = Particle(axis_length, stuck_list)
        # particle.generate_initial_position()
        # particle.print_particle_position()
        # dist = np.linalg.norm([particle.get_particle_position(), stuck_list[0]])
        # self.assertTrue(dist > axis_length/2), f'{dist}'
        

class TestParticleWalk(unittest.TestCase):
    
    def test_is_frozen(self):
        """
        Test to determine if a walking particle gets frozen when it comes into 
        contact with an existing part of the cluster.

        Check: If [x+1, y] or [x-1, y] or [x, y+1] or [x, y-1] = [m, n] 
        in stuck_list particle is stuck and its position should be appended
        to stuck_list.
        """
        pass

    def test_at_boundary(self):
        """
        Test to determine if a walking particle exits the lattice while at the
        boundary.

        Check: If x,y == axis_length particle is at the boundary and should 
        exit (self.on_lattice = False)

        Cases: 1. on the x boundary           at_boundary() == True
               2. on the y boundary           at_boundary() == True
               3. on the x and y boundary     at_boundary() == True
               4. not on the boundary         at_boundary() == False
        """
        axis_length = 10
        stuck_list = [[0, 0]]

        particles = [Particle(axis_length, stuck_list) for i in range(0,4)]            
            
        particles[0].x = 10                          # Case 1
        particles[1].y = 10                          # Case 2
        particles[2].x, particles[2].y = 10, 10      # Case 3
        particles[3].x, particles[3].y = 5, 5        # Case 4

        for particle in particles:
            particle.at_boundary()
     
        self.assertFalse(particles[0].on_lattice)
        self.assertFalse(particles[1].on_lattice)
        self.assertFalse(particles[2].on_lattice)
        self.assertTrue(particles[3].on_lattice)

    def test_take_step(self):
        """
        Test to make sure that the particle moves one and only one step away
        and in one of four directions (UP, DOWN, LEFT, RIGHT)

        Check: If (x,y)_n+1 has x OR y value one greater than (x,y)_n
        """
        pass

    def test_direction_dist(self):
        """
        Test to make sure that all directions (UP, DOWN, LEFT, RIGHT) have an
        equal chance of being visited
        """
        pass

    

if __name__ == '__main__':
    unittest.main()
