import matplotlib.pyplot as plt
import numpy as np


def get_subtitles(ax=None, x=0, y=0, subtitle="", **kwags):
    if ax is None:
        ax = plt

    return ax.text(x=x, y=y, s=subtitle, **kwags)

