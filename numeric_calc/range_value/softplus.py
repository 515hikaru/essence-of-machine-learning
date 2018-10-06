import numpy as np

def softplus(x):
    """
    log(1 + e^x)

    np.exp を評価してから log をとるため実際の値としては小さくても
    計算機的にはオーバーフローをしてしまうケースがある
    """
    return np.log(1 + np.exp(x))


def softplus2(x):
    """
    max(x, 0) + log(1 + e^{-|x|})

    オーバーフローをしないように同値な式に書き換え
    """
    return max(0, x) + np.log(1 + np.exp(-abs(x)))
