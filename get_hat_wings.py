import matplotlib.pyplot as plt
import numpy as np
from get_rotate import rotate


def get_hat_wings(
    r: float = 1,
    q: int = 1000,
    ax=None,
    x=0.0,
    y=0.0,
    h1=1.0,
    color="yellow",
    edgecolor="black",
    degree=90.0,
    zorder=1,
    lw=2,
    **kwags,
):
    if ax is None:
        ax = plt
    _x = np.linspace(-r + x, r + x, q)
    _y = lambda _x: -np.sqrt(r ** 2 - (_x - x) ** 2) * h1

    _x, _y = rotate(_x, _y(_x), degree,)
    _x, _y = _x + x, _y + y
    ax.plot(_x, _y, color=edgecolor, zorder=zorder, lw=lw, **kwags)
    ax.fill(_x, _y, color=color, zorder=zorder, lw=lw, **kwags)
