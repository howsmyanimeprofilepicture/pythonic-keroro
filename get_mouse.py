import matplotlib.pyplot as plt
import numpy as np


def get_mouse(
    ax=None,
    r=1.0,
    y=2.6,
    coeff=0,
    color="red",
    edgecolor="black",
    zorder=1,
    lw=2,
    **kwags,
):

    x = np.linspace(-r, r, 100)

    if ax is None:
        ax = plt

    answer = ax.fill_between(
        x,
        0.7 * np.cos(x) - y - 0.3,
        coeff * -0.7 * np.cos(np.pi * x / 2) - y,
        zorder=zorder,
        color=color,
        lw=lw,
        edgecolor=edgecolor,
        **kwags,
    )
    return answer
