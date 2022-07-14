import matplotlib.pyplot as plt
import numpy as np


def get_skin(
    r: float = 1,
    q: int = 1000,
    ax=None,
    x=0.0,
    y=0.0,
    color="green",
    z=0.5,
    mouse_rad=1.5,
    lw=2,
    **kwags,
):
    if ax is None:
        ax = plt
    _x = np.linspace(-r + x, r + x, q)
    f_2 = lambda _x: -np.sqrt(r ** 2 - (_x - x) ** 2) + y
    f_3 = lambda _x: -(_x ** 2) + z ** 2

    _y2 = list(
        map(
            lambda item_x: (
                f_2(item_x) if np.abs(item_x) > z else f_2(z) + mouse_rad * f_3(item_x)
            ),
            _x,
        )
    )

    return ax.fill_between(
        _x, np.sqrt(r ** 2 - (_x - x) ** 2) + y, _y2, lw=lw, color=color, **kwags,
    )

