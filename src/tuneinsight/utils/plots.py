from pathlib import Path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


this_path = str(Path(__file__).parent)


def style_plot(axis:plt.Axes, fig, title, x_label, y_label, size:tuple = (8,4), local=False):
    font_light = Path(this_path + "/graphical/MontserratLight.ttf")
    font_regular = Path(this_path + "/graphical/MontserratRegular.ttf")
    font_med = Path(this_path + "/graphical/MontserratMedium.ttf")

    axis.set_ylabel(y_label, font=font_med, fontsize=10)
    axis.set_xlabel(x_label, font=font_med, fontsize=10)
    axis.set_title(title, font=font_regular, fontsize=15)

    plt.xticks(font=font_regular, fontsize=8)
    plt.yticks(font=font_regular, fontsize=8)

    fig.set_size_inches(size[0],size[1])
    fig.tight_layout()

    if not local:
        plt.text(0.5, -0.15, "The computation of these results was made possible by Tune Insight's Federated Confidential Computing.", horizontalalignment='center',
        verticalalignment='top',
        transform=axis.transAxes,
        font=font_light,
        fontsize=8)


        logo = Image.open(this_path + "/graphical/TuneInsight_logo.png")
        rsize = logo.resize((np.array(logo.size)/4).astype(int))

        axis.figure.figimage(rsize, 10, 0, alpha=0.9, zorder=1)

def style_title(axis, title = "", fontsize=15):
    font_regular = Path(this_path + "/graphical/MontserratRegular.ttf")
    axis.set_title(title, font=font_regular, fontsize=fontsize)

def style_ylabel(axis, y_label, fontsize=10):
    font_med = Path(this_path + "/graphical/MontserratMedium.ttf")
    axis.set_ylabel(y_label, font=font_med, fontsize=fontsize)

def add_ti_branding(axis: plt.Axes, x=1.5, ha='center', local=False):
    if not local:
        font_light = Path(this_path + "/graphical/MontserratLight.ttf")
        ymin, ymax = axis.get_ylim()
        adjust = 0.1 * (ymax-ymin)
        plt.text(x, ymin - adjust, "The computation of these results was made possible by Tune Insight's Federated Confidential Computing.",
            horizontalalignment=ha,
            verticalalignment='top',
            font=font_light,
            fontsize=8)

        logo = Image.open(this_path + "/graphical/TuneInsight_logo.png")
        rsize = logo.resize((np.array(logo.size)/4).astype(int))

        axis.figure.figimage(rsize, 10, 0, alpha=0.9, zorder=1)

def hist(x, title, bins=30, hist_range=(0,30), local=True):

    plt.style.use("bmh")

    # plot
    fig, ax = plt.subplots()


    ax.hist(x,bins=bins,range=hist_range, color="#D05F5C", edgecolor='black')


    style_plot(ax, fig, title, "","", size=(6,4), local=local)

    plt.show()

def get_path():
    print(Path(__file__).parent)
