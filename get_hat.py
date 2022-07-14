import matplotlib.pyplot as plt
import numpy as np


def get_hat(
    r: float = 1,
    q: int = 1000,
    ax=None,
    x=0.0,
    y=0.0,
    h1=1.0,
    h2=1.0,
    color="yellow",
    edgecolor="black",
    z=0.1,
    lw=2,
    **kwags,
):
    if ax is None:
        ax = plt
    _x = np.linspace(-r + x, r + x, q)
    _y_1 = lambda _x: np.sqrt(r ** 2 - (_x - x) ** 2) * h1 + y
    _y_2 = lambda _x: np.sqrt(r ** 2 - (_x - x) ** 2) * h2 + y
    ax.fill_between(
        _x, _y_1(_x), _y_2(_x), color=color, lw=lw, **kwags,
    )

    top_line = ax.plot(_x, _y_1(_x), color=edgecolor, lw=lw, **kwags)
    __x = np.linspace(-r + x + z, r + x - z, q)
    bot_line = ax.plot(__x, _y_2(__x), color=edgecolor, linewidth=lw, **kwags)
