import matplotlib.pyplot as plt
import numpy as np


def get_circle(
    r: float = 1,
    q: int = 1000,
    ax=None,
    x=0.0,
    y=0.0,
    z=0.5,
    color="black",
    lw=2,
    **kwags,
):
    if ax is None:
        ax = plt
    _x = np.linspace(-r + x, r + x, q)
    _y1 = np.sqrt(r ** 2 - (_x - x) ** 2) + y

    f_2 = lambda _x: -np.sqrt(r ** 2 - (_x - x) ** 2) + y

    return ax.fill_between(_x, _y1, f_2(_x), lw=lw, color=color, **kwags,)
