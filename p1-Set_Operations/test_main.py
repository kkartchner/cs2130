__author__ = "Ky Kartchner"
__date__ = "11 May 2020"

from random import randint
import unittest
import set_operations as ops

class TestOperations(unittest.TestCase):
    def randomSet(self):
        ''' Generate a random set '''
        randSet = set() # create empty set
        rand_length = randint(0, 100) # get random length for set

        while len(randSet) < rand_length: 
            # add random numbers between 0 and the set length*2 
            # (to ensure enough options)
            randSet.add(randint(0, rand_length*2))

        return randSet

    def test_union(self):
        ''' Test union function '''
        for _ in range(1000):
            setA = self.randomSet() # create random set 
            setB = self.randomSet() # create random set
            # make sure that union set is the same as built in union function:
            self.assertEqual(ops.union(setA, setB), setA.union(setB))
            # test equal set scenario to make sure it results in the set itself:
            self.assertEqual(ops.union(setA, setA), setA) 

    def test_intersection(self):
        ''' Test intersection function '''
        for _ in range(1000):
            setA = self.randomSet()
            setB = self.randomSet()
            # make sure that the intersect set is the same as built in intersection function:
            self.assertEqual(ops.intersect(setA, setB), setA.intersection(setB))
            # test equal set scenario to make sure it results in the set itself:
            self.assertEqual(ops.intersect(setA, setA), setA)
    
    def test_difference(self):
        ''' Test difference function '''
        for _ in range(1000):
            setA = self.randomSet()
            setB = self.randomSet()
            # make sure that the difference set is the same as built in difference function:
            self.assertEqual(ops.difference(setA, setB), setA.difference(setB))
            # test equal set scenario to make sure it results in the empty set:
            self.assertEqual(ops.difference(setA, setA), set())
        

if __name__ == '__main__':
    unittest.main()
