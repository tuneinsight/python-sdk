"""Visual utilities for plots with Tune Insight branding."""

from pathlib import Path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


HERE = str(Path(__file__).parent)

FONT_LIGHT = Path(HERE + "/graphical/MontserratLight.ttf")
FONT_REGULAR = Path(HERE + "/graphical/MontserratRegular.ttf")
FONT_MED = Path(HERE + "/graphical/MontserratMedium.ttf")


def style_plot(
    axis: plt.Axes,
    fig: plt.figure,
    title: str,
    x_label: str,
    y_label: str,
    size: tuple = (8, 4),
    local=False,
):
    """
    Style a plot with Tune Insight branding.

    This modifies the plot given by 'axis' by using the appropriate fonts, adding
    the Tune Insight logo, and branding text if the computation is not local.

    Args:
        axis (plt.Axes): axis on which to apply styling
        fig (plt.figure): figure on which to apply styling
        title (str): plot title
        x_label (str): x label of plot
        y_label (str): y label of plot
        size (tuple, optional): plot size. Defaults to (8,4).
        local (bool, optional): whether or not the plot is for results of a local computation. Defaults to False.
    """

    style_label(axis, x_label=x_label, y_label=y_label, fontsize=10)
    style_title(axis, title, fontsize=15)

    plt.xticks(font=FONT_REGULAR, fontsize=8)
    plt.yticks(font=FONT_REGULAR, fontsize=8)

    fig.set_size_inches(size[0], size[1])
    fig.tight_layout()

    add_ti_branding(axis, local=local)


def style_title(axis: plt.Axes, title: str = "", fontsize: int = 15):
    """
    Style plot title with Tune Insight branding font.

    Args:
        axis (plt.Axes): axis on which to apply styling
        title (str, optional): plot title. Defaults to "".
        fontsize (int, optional): title fontsize. Defaults to 15.
    """
    axis.set_title(title, font=FONT_REGULAR, fontsize=fontsize)


def style_suptitle(fig, title="", fontsize=15):
    """
    Style the suptitle of a figure with Tune Insight branding font

    Args:
        fig: the figure to style.
        title (str, optional): figure suptitle. Defaults to "".
        fontsize (int, optional): suptitle fontsize. Defaults to 15.
    """
    fig.suptitle(title, font=FONT_REGULAR, size=fontsize)


def style_label(
    axis: plt.Axes,
    x_label: str = None,
    y_label: str = None,
    fontsize: int = 10,
):
    """
    Style the x and/or y (default) labels of a plot with Tune Insight branding font.

    Args:
        axis (plt.Axes): axis on which to apply styling
        x_label (str, optional): The x label to write. If None, no styling is applied.
        y_label (str, optional): The y label to write. If None, no styling is applied.
        fontsize (int, optional): label fontsize. Defaults to 10.
    """
    args = {"font": FONT_MED, "fontsize": fontsize}
    if x_label:
        axis.set_xlabel(x_label, **args)
    if y_label:
        axis.set_ylabel(y_label, **args)


def add_ti_branding(axis: plt.Axes, local=False):
    """
    Add Tune Insight logo and credits.

    Args:
        axis (plt.Axes): axis on which to add branding
        local (bool, optional): whether or not the plot is for results of a local computation.
            Defaults to False.
    """
    # Get axis coordinates to infer the location of the branding.
    xmin, xmax = axis.get_xlim()
    xmargin = 0.05 * (xmax - xmin)
    ymin, ymax = axis.get_ylim()
    ymargin = 0.1 * (ymax - ymin)

    # This is the top baseline of all branding material.
    ybaseline = ymin - ymargin

    if not local:
        plt.text(
            xmax + xmargin,  # Extends the plot 5% to the right.
            ybaseline,
            "The computation of these results was made possible by Tune Insight's Federated Confidential Computing.",
            horizontalalignment="right",
            verticalalignment="top",
            font=FONT_LIGHT,
            fontsize=8,
        )

    logo = Image.open(HERE + "/graphical/TuneInsight_logo.png")
    rsize = logo.resize((np.array(logo.size) / 4).astype(int))

    axis.figure.figimage(rsize, xmin, ybaseline, alpha=0.9, zorder=1)


def hist(x, title, bins=30, hist_range=(0, 30), local=True):
    """
    Plot a histogram with Tune Insight branding.

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

    ax.hist(x, bins=bins, range=hist_range, color="#D05F5C", edgecolor="black")

    style_plot(ax, fig, title, "", "", size=(6, 4), local=local)

    plt.show()
