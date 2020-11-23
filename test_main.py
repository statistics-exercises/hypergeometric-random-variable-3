import unittest
import scipy.stats
from main import *

class UnitTests(unittest.TestCase) :
    def test_function(self) :
        for M in range(2,4) :
            for N in range(5,7) : 
                for R in range(1,N) : 
                    mean = 0 
                    for k in range(100) : mean = mean + hypergeometric_random_variable(M,R,N) 
                    prob = R/N
                    var = M*prob*((N-R)/N)*(N-M)/(N-1)
                    bar = np.sqrt(var/100)*scipy.stats.norm.ppf( (0.99 + 1) / 2 )
                    self.assertTrue( np.fabs( mean/100 - M*prob )<bar, "Your function for generating the random variable is not working correctly" )
