from pathlib import Path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


this_path = str(Path(__file__).parent)


def style_plot(axis:plt.Axes, fig:plt.figure, title:str, x_label:str, y_label:str, size:tuple = (8,4), local=False):
    """ Style a plot with Tune Insight branding

    Args:
        axis (plt.Axes): axis on which to apply styling
        fig (plt.figure): figure on which to apply styling
        title (str): plot title
        x_label (str): x label of plot
        y_label (str): y label of plot
        size (tuple, optional): plot size. Defaults to (8,4).
        local (bool, optional): whether or not the plot is for results of a local computation. Defaults to False.
    """
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

def style_title(axis: plt.Axes, title:str = "", fontsize:int = 15):
    """ Style plot title with Tune Insight branding font.

    Args:
        axis (plt.Axes): axis on which to apply styling
        title (str, optional): plot title. Defaults to "".
        fontsize (int, optional): title fontsize. Defaults to 15.
    """
    font_regular = Path(this_path + "/graphical/MontserratRegular.ttf")
    axis.set_title(title, font=font_regular, fontsize=fontsize)

def style_ylabel(axis: plt.Axes, y_label: str, fontsize: int = 10):
    """ Style plot y label with Tune Insight branding font

    Args:
        axis (plt.Axes): axis on which to apply styling
        y_label (str): plot y label
        fontsize (int, optional): label fontsize. Defaults to 10.
    """
    font_med = Path(this_path + "/graphical/MontserratMedium.ttf")
    axis.set_ylabel(y_label, font=font_med, fontsize=fontsize)

def add_ti_branding(axis: plt.Axes, x=1.5, ha='center', local=False):
    """ Add Tune Insight logo and credits

    Args:
        axis (plt.Axes): axis on which to add branding
        x (float, optional): x coordinate of credit text. Defaults to 1.5.
        ha (str, optional): horizontal alignment of credit text. Defaults to 'center'.
        local (bool, optional): whether or not the plot is for results of a local computation. Defaults to False.
    """
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
    """ Create histogram with Tune Insight branding.

    Args:
        x (_type_): values to plot
        title (_type_): plot title
        bins (int, optional): number of bins. Defaults to 30.
        hist_range (tuple, optional): histogram range. Defaults to (0,30).
        local (bool, optional): whether or not the plot is for results of a local computation. Defaults to True.
    """

    plt.style.use("bmh")

    # plot
    fig, ax = plt.subplots()


    ax.hist(x,bins=bins,range=hist_range, color="#D05F5C", edgecolor='black')


    style_plot(ax, fig, title, "","", size=(6,4), local=local)

    plt.show()

def get_path():
    print(Path(__file__).parent)
