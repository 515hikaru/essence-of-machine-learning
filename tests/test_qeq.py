import unittest

from numeric_calc.quad_equation import qeq

class TestQuadEquation(unittest.TestCase):
    """
    2次方程式を解くテスト 
    """
    def test_solve_simple_eq(self):
        """x^2+5x+6を解く"""
        eps = 1e-18
        alpha, beta = qeq.qeq(1, 5, 6)
        self.assertAlmostEqual(alpha, -2.0, delta=eps)
        self.assertAlmostEqual(beta, -3.0, delta=eps)

    def test_solve_simple_eq2(self):
        """x^2-5x+6を解く"""
        eps = 1e-18
        alpha, beta = qeq.qeq(1, -5, 6)
        self.assertAlmostEqual(alpha, 3.0, delta=eps)
        self.assertAlmostEqual(beta, 2.0, delta=eps)

    def test_solve_less_error_eq(self):
        """x^2+5x+6を解く"""
        eps = 1e-18
        alpha, beta = qeq.qeq2(1, 5, 6)
        self.assertAlmostEqual(alpha, -3.0, delta=eps)
        self.assertAlmostEqual(beta, -2.0, delta=eps)

    def test_solve_less_error_eq2(self):
        """x^2-5x+6を解く"""
        eps = 1e-18
        alpha, beta = qeq.qeq2(1, -5, 6)
        self.assertAlmostEqual(alpha, 3.0, delta=eps)
        self.assertAlmostEqual(beta, 2.0, delta=eps)

    def test_solve_error_large(self):
        """
        誤差が大きくなるテストケース
        (x+0.000000001)(x+1) = 0
        """
        eps = 1e-18
        alpha, beta = qeq.qeq2(1, 1.000000001, 0.000000001)
        self.assertAlmostEqual(alpha, -1.0, delta=eps)
        self.assertAlmostEqual(beta, -1e-9, delta=eps)
