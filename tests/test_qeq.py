import unittest

import pytest

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

    @pytest.mark.xfail
    def test_solve_error_large_fail(self):
        """
        誤差が大きくなるテストケース
        誤差対策ができていないケースなのでこのテストは失敗する
        (x+0.000000001)(x+1) = 0
        """
        eps = 1.0 * (10 ** (-18))
        alpha, beta = qeq.qeq(1, 1.000000001, 0.000000001)
        self.assertAlmostEqual(beta, -1.0, delta=eps)
        self.assertAlmostEqual(alpha, -0.000000001, delta=eps)  # fail here

    def test_solve_error_large(self):
        """
        誤差が大きくなるテストケース
        (x+0.000000001)(x+1) = 0
        """
        eps = 1e-18
        alpha, beta = qeq.qeq2(1, 1.000000001, 0.000000001)
        self.assertAlmostEqual(alpha, -1.0, delta=eps)
        self.assertAlmostEqual(beta, -0.000000001, delta=eps)
