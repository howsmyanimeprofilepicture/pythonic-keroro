import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

from get_hat_wings import get_hat_wings
from get_circle import get_circle
from get_skin import get_skin
from get_mouse import get_mouse
from get_hat import get_hat
from get_subtitles import get_subtitles
from get_prompt import get_prompt


def main():
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])

    get_hat_wings(ax=ax, x=1.42, y=1, r=1.3, h1=4, degree=20)
    get_hat_wings(ax=ax, x=-1.42, y=1, r=1.3, h1=4, degree=-20)

    get_circle(ax=ax, x=0, y=0, r=4, color="white", edgecolor="black", zorder=2)
    skin = get_skin(zorder=3, r=4, z=2, mouse_rad=0.3, edgecolor="black")

    get_circle(ax=ax, x=-2, y=0, r=1.5, color="white", edgecolor="black", zorder=4)
    get_circle(ax=ax, x=2, y=0, r=1.5, color="white", edgecolor="black", zorder=4)

    get_circle(ax=ax, x=-2, y=0, r=1, zorder=5)
    get_circle(ax=ax, x=2, y=0, r=1, zorder=5)
    get_hat(ax=ax, color="yellow", y=1.2, r=4.2, h1=0.8, h2=0.2, z=0.5, zorder=6)

    global mouse
    mouse = get_mouse(ax=ax)
    global PROMPT
    PROMPT = get_prompt()
    global char_list
    char_list = list(PROMPT.pop(0))
    # print(char_list)
    global subs
    subs = get_subtitles(
        ax=ax,
        x=1,
        y=-7,
        subtitle="",
        fontsize=25,
        horizontalalignment="center",
        verticalalignment="center",
    )

    def update(i):
        global mouse
        coeff = (np.sin(i * np.pi / 8) + 1) / 2
        mouse.remove()
        mouse = get_mouse(coeff=coeff, ax=ax)

        global subs
        global char_list
        global PROMPT

        if i % 3 == 0:
            pre_text = subs.get_text()
            if char_list.__len__() == 0:
                pre_text = ""
                char_list = list(PROMPT.pop(0))
            if len(PROMPT) == 0:
                PROMPT = get_prompt()

            subs.set_text(pre_text + char_list.pop(0))

        return (mouse, subs)

    ani = animation.FuncAnimation(fig, update, interval=20, frames=200, blit=True)

    plt.show()


if __name__ == "__main__":
    main()
