import numpy as np
import pytest

from numeric_calc.range_value import softplus


def test_softplus_value1():
    """
    np.exp がオーバーフローしない範囲での計算

    log(1+e^{-1}) の計算
    """
    y = softplus.softplus(-1)
    assert isinstance(y, np.float64)
    assert y > 0

def test_softplus_value2():
    """
    np.exp がオーバーフローしない範囲での計算
    
    log(1+1) の計算
    """            
    y = softplus.softplus(0)
    assert y == np.log(2)

@pytest.mark.xfail
def test_softplus_inf():
    """
    np.exp がオーバーフローしたときの計算

    このテストは対策ができていないので失敗する
    """
    y = softplus.softplus(1000)
    assert y < 10 * 5

def test_softplus2_value1():
    """
    np.exp がオーバーフローしない範囲での計算

    log(1+e^{-1}) の計算
    """
    y = softplus.softplus2(-1)
    assert isinstance(y, np.float64)
    assert y > 0

def test_softplus2_value2():
    """
    np.exp がオーバーフローしない範囲での計算
    
    log(1+1) の計算
    """            
    y = softplus.softplus2(0)
    assert y == np.log(2)

def test_softplus2_inf():
    """
    np.exp をそのまま計算するとオーバーフローする場合
    
    対策済みなのでこのテストではオーバーフローせず成功する
    """
    y = softplus.softplus2(1000)
    assert y < 10 ** 4
