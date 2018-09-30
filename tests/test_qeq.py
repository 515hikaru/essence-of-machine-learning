import unittest

from numeric_calc.quad_equation import qeq

class TestQuadEquation(unittest.TestCase):
    """
    2次方程式を解くテスト 
    """
    def test_solve_simple_eq(self):
        """x^2+5x+6を解く"""
        eps = 1e-10
        alpha, beta = qeq.qeq(1, 5, 6)
        self.assertAlmostEqual(alpha, -2.0, eps)
        self.assertAlmostEqual(beta, -3.0, eps)

    def test_solve_simple_eq2(self):
        """x^2-5x+6を解く"""
        eps = 1e-10
        alpha, beta = qeq.qeq(1, -5, 6)
        self.assertAlmostEqual(alpha, 3.0, eps)
        self.assertAlmostEqual(beta, 2.0, eps)
