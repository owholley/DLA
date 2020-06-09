# Test the DLA algorithm
# Going to write tests as if there is no program, then rebuild the algorithm
import unittest

from particle import Particle
        

class TestParticleWalk(unittest.TestCase):

    def test_take_step(self):
        """
        Test to make sure that the particle moves one and only one step away
        and in one of four directions (UP, DOWN, LEFT, RIGHT)

        Check: If (x,y)_n+1 has x OR y value one greater than (x,y)_n

        Case 1: Move UP: [x, y+1]
        Case 2: Move DOWN: [x, y-1]
        Case 3: Move RIGHT: [x+1, y]
        Case 4: Move LEFT: [x-1, y]
        """
        pass


class TestIsFrozen(unittest.TestCase):

    """
    Class to test is_frozen(). 

    Need to test six(?) possible cases. A frozen particle is one UP from the
    current particle position, a frozen particle is one DOWN from the current
    particle position, a frozen particle is one LEFT from the current particle
    position, a frozen particle is one RIGHT from the current particle 
    position, there are frozen particle is in TWO directions (for example one 
    UP and one LEFT) from the current particle position, and finally, there are
    no frozen particles one step away from the current particle position in any
    direction.

    Case 1: UP    [x, y+1] in stuck_list
    Case 2: DOWN  [x, y-1] in stuck_list
    Case 3: LEFT  [x-1, y] in stuck_list
    Case 4: RIGHT [x+1, y] in stuck_list
    Case 5: TWO   [x, y+1], [x-1, y] in stuck_list
    Case 6: NONE  none of the above cases apply
    """

    def test_up_is_frozen(self):
        
        """
        Test to determine if is_frozen() correctly identifies a walking 
        particle as frozen if the position one UP from the current position
        is in stuck_list (is part of the cluster).

        Case: UP    [x, y+1] in stuck_list
        """
        particle = Particle(axis_length=10, stuck_list=[[0, 0],])
        particle.x, particle.y = -1, 0
        particle.is_frozen()
        self.assertTrue(particle.frozen)

    def test_down_is_frozen(self):
        """
        Test to determine if is_frozen() correctly identifies a walking
        particle as frozen if the position one DOWN from the current position
        is in stuck_list (is part of the cluster).

        Case: DOWN    [x, y-1] in stuck_list
        """
        particle = Particle(axis_length=10, stuck_list=[[0, 0],])
        particle.x, particle.y = 0, 1
        particle.is_frozen()
        self.assertTrue(particle.frozen)

    def test_left_is_frozen(self):
        """
        Test to determine if is_frozen() correctly identifies a walking
        particle as frozen if the position one LEFT from the current position
        is in stuck_list (is part of the cluster).

        Case: LEFT    [x-1, y] in stuck_list
        """
        particle = Particle(axis_length=10, stuck_list=[[0, 0],])
        particle.x, particle.y = 1, 0
        particle.is_frozen()
        self.assertTrue(particle.frozen)
        
    def test_right_is_frozen(self):
        """
        Test to determine if is_frozen() correctly identifies a walking
        particle as frozen if the position one RIGHT from the current position
        is in stuck_list (is part of the cluster).

        Case: RIGHT    [x+1, y] in stuck_list
        """
        particle = Particle(axis_length=10, stuck_list=[[0, 0],])
        particle.x, particle.y = -1, 0
        particle.is_frozen()
        self.assertTrue(particle.frozen)
        
    def test_two_is_frozen(self):
        """
        Test to determine if is_frozen() correctly identifies a walking
        particle as frozen if two of the positions one step away contain frozen
        particles (in this case UP and LEFT)

        Case: TWO  UP & LEFT    [x+1, y] in stuck_list
        """
        particle = Particle(
            axis_length=10,
            stuck_list=[[0, 0], [-1, 0],]
        )
        particle.x, particle.y = 0, -1
        particle.is_frozen()
        self.assertTrue(particle.frozen)
    
    def test_not_frozen_particle_is_frozen(self):
        """
        Test to determine if is_frozen() correctly leaves an unfrozen particle
        set to self.frozen = False

        Case: None of the four possible sites the particle could move to are in
              stuck_list
        """
        particle = Particle(10, [[0, 0],])
        particle.x, particle.y = 5, 5   # Nowhere near stuck_list = [[0, 0],]
        particle.is_frozen()
        self.assertFalse(particle.frozen)

class TestAtBoundary(unittest.TestCase):

    """
    Class to test at_boundary().
    
    Need to test four possible cases, particle on the x boundary, particle
    on the y boundary, particle on both the x and y boundaries, and a particle
    neither on the x or y boundaries.

    Case 1: x = axis_length
    Case 2: y = axis_length
    Case 3: x,y = axis_length
    Case 4: x,y < axis_length
    """

    def test_particle_at_x_boundary(self):
        """
        Test to determine if the at_boundary() function correctly identifies a
        particle that is touching the x boundary.

        Case: x = axis_length
        """
        particle = Particle(axis_length=10, stuck_list=[[0, 0],])
        particle.x = 10           # set x = axis_length
        particle.at_boundary()
        self.assertFalse(particle.on_lattice)

    def test_particle_at_y_boundary(self):
        """
        Test to determine if the at_boundary() function correctly identifies a 
        particle that is touching the y boundary.

        Case: y = axis_length
        """
        particle = Particle(axis_length=10, stuck_list=[[0, 0],])
        particle.y = 10           # set y = axis_length
        particle.at_boundary()
        self.assertFalse(particle.on_lattice)

    def test_particle_at_x_and_y_boundaries(self):
        """
        Test to determine if the at_boundary() function correctly identifies a
        particle that is touching the y boundary.

        Case x,y = axis_length
        """
        particle = Particle(axis_length=10, stuck_list=[[0, 0],])
        particle.x, particle.y = 10, 10   # set x,y = axis_length
        particle.at_boundary()
        self.assertFalse(particle.on_lattice)

    def test_particle_not_at_boundary(self):
        """
        Test to determine if at_boundary() correctly labels particle.on_lattice
        as True for a particle which is not touching the boundary

        Case: x,y < axis_length
        """
        particle = Particle(axis_length=10, stuck_list=[[0, 0],])
        particle.x, particle.y = 5, 5   # x,y < axis_length
        particle.at_boundary()
        self.assertTrue(particle.on_lattice)


class TestWalkParticle(unittest.TestCase):
    
    """
    Class to test walk_particle()
    """

if __name__ == '__main__':
    unittest.main()
