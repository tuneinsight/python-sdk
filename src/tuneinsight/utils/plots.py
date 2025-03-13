"""Visual utilities for plots with Tune Insight branding."""

from pathlib import Path
from typing import List
from PIL import Image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


HERE = str(Path(__file__).parent)

FONT_LIGHT = Path(HERE + "/graphical/MontserratLight.ttf")
FONT_REGULAR = Path(HERE + "/graphical/MontserratRegular.ttf")
FONT_MED = Path(HERE + "/graphical/MontserratMedium.ttf")


TI_COLORS = [
    # Tart Red
    "#F05454",
    # Charcoal
    "#30475E",
    # Mustard
    "#FFDD56",
    # Emerald
    "#65BF7D",
]
# Gunmetal color for labels and ticks
PLOT_LABEL_COLOR = "#222831"
PLOT_EDGE_COLOR = PLOT_LABEL_COLOR
PLOT_TICK_COLOR = PLOT_LABEL_COLOR
PLOT_TITLE_COLOR = PLOT_LABEL_COLOR


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
    Styles a plot with Tune Insight branding.

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
    axis.grid(False)

    plt.xticks(font=FONT_REGULAR, fontsize=10, color=PLOT_TICK_COLOR)
    plt.yticks(font=FONT_REGULAR, fontsize=10, color=PLOT_TICK_COLOR)

    fig.set_size_inches(size[0], size[1])
    fig.tight_layout()

    add_ti_branding(axis, local=local)


def style_title(axis: plt.Axes, title: str = "", fontsize: int = 15):
    """
    Styles the title of a plot with Tune Insight branding font.

    Args:
        axis (plt.Axes): axis on which to apply styling
        title (str, optional): plot title. Defaults to "".
        fontsize (int, optional): title fontsize. Defaults to 15.
    """
    axis.set_title(title, font=FONT_REGULAR, fontsize=fontsize, color=PLOT_TITLE_COLOR)


def style_suptitle(fig, title="", fontsize=15):
    """
    Styles the suptitle of a figure with Tune Insight branding font.

    Args:
        fig: the figure to style.
        title (str, optional): figure suptitle. Defaults to "".
        fontsize (int, optional): suptitle fontsize. Defaults to 15.
    """
    fig.suptitle(title, font=FONT_REGULAR, size=fontsize, color=PLOT_TITLE_COLOR)


def style_label(
    axis: plt.Axes,
    x_label: str = None,
    y_label: str = None,
    fontsize: int = 10,
):
    """
    Styles the x and/or y (default) labels of a plot with Tune Insight branding font.

    Args:
        axis (plt.Axes): axis on which to apply styling
        x_label (str, optional): The x label to write. If None, no styling is applied.
        y_label (str, optional): The y label to write. If None, no styling is applied.
        fontsize (int, optional): label fontsize. Defaults to 10.
    """
    args = {"font": FONT_MED, "fontsize": fontsize, "color": PLOT_LABEL_COLOR}
    if x_label:
        axis.set_xlabel(x_label, **args)
    if y_label:
        axis.set_ylabel(y_label, **args)


def add_ti_branding(axis: plt.Axes, local=False):
    """
    Adds Tune Insight logo and credits.

    Args:
        axis (plt.Axes): axis on which to add branding
        local (bool, optional): whether or not the plot is for results of a local computation.
            Defaults to False.
    """

    text = "The computation of these results was made possible by Tune Insight's Federated Confidential Computing."
    space_pad_value = 8
    text = " " * space_pad_value + text + " " * space_pad_value

    if not local:
        plt.text(
            0.5,
            -0.05,
            text,
            horizontalalignment="center",
            verticalalignment="top",
            font=FONT_LIGHT,
            fontsize=9,
            transform=plt.gcf().transFigure,
        )

    logo = Image.open(HERE + "/graphical/TuneInsight_logo.png")
    rsize = logo.resize(tuple((np.array(logo.size) / 4).astype(int)))

    axis.figure.figimage(
        rsize,
        0,
        0,
        alpha=0.9,
        zorder=1,
        origin="upper",
    )


def add_branded_text(
    axis: plt.Axes,
    text: str,
    x: float,
    y: float,
    fontsize: int = 9,
    horizontalalignment="center",
    verticalalignment="top",
    rotation=0,
):
    """
    Adds branded text to the plot.

    Args:
        axis (plt.Axes): axis on which to add text
        text (str): text to add
        x (float): x coordinate of text
        y (float): y coordinate of text
        fontsize (int, optional): fontsize of text. Defaults to 9.
    """
    axis.text(
        x,
        y,
        text,
        horizontalalignment=horizontalalignment,
        verticalalignment=verticalalignment,
        font=FONT_LIGHT,
        fontsize=fontsize,
        rotation=rotation,
    )


HISTOGRAM_LINE_WIDTH = 1.0
BAR_DEFAULT_WIDTH = 0.8
# The percentage of empty space on top of the largest bar in the plot.
BAR_Y_EMPTY_PERCENT = 0.25


def hist(
    x, y, title: str = "", x_label="", y_label="", local=False, size: tuple = (8, 4)
):
    """
    Plots a histogram with Tune Insight branding.

    Args:
        x (ArrayLike): the list of x values.
        y (ArrayLike): the list of y values.
        title (str, optional): optional plot title.
        x_label (str, optional): optional x label. Defaults to "".
        y_label (str, optional): optional y axis label. Defaults to "".
        local (bool, optional): whether the plotting corresponds to local results. Defaults to False.
        size (tuple, optional): size of the plot. Defaults to (8, 4).
    """

    max_value = max(y)

    plt.style.use("bmh")
    # plot
    fig, ax = plt.subplots()
    rects = ax.bar(
        x,
        y,
        color=TI_COLORS[0],
        edgecolor=PLOT_EDGE_COLOR,
        linewidth=HISTOGRAM_LINE_WIDTH,
    )
    ax.bar_label(
        rects,
        padding=4,
        label_type="edge",
        fontsize=9,
        font=FONT_MED,
        color=PLOT_LABEL_COLOR,
    )
    ax.set_ylim(0, max_value + max_value * BAR_Y_EMPTY_PERCENT)
    style_plot(ax, fig, title, x_label, y_label, size=size, local=local)
    plt.show()


def hist_grouped(
    group: str,
    variables: List[str],
    result: pd.DataFrame,
    title: str = "",
    x_label: str = "",
    y_label: str = "",
    size=(8, 4),
):
    """
    Plots the data in a grouped histogram / bar plot with Tune Insight branding.

    Args:
        group (str): the group to plot from the data points.
        variables (List[str]): the list of variables to plot per-group
        result (pd.DataFrame): the data frame containing the data to plot.
        title (str, optional): optional plot title. Defaults to "".
        x_label (str, optional): optional plot xlabel. Defaults to "".
        y_label (str, optional): optional plot ylabel. Defaults to "".
        size (tuple, optional): optional plot size tuple. Defaults to (8, 4).
    """
    plt.style.use("bmh")
    fig, ax = plt.subplots()
    categories = list(result[group])
    x = np.arange(len(categories))
    width = BAR_DEFAULT_WIDTH
    if len(variables) > 0:
        width = 1.0 / (len(variables) + 0.5)

    multiplier = 0
    max_value = 0
    bottom = np.zeros(len(result))

    for var in variables:

        y = result[var]
        max_value = max(y + [max_value])
        offset = width * multiplier

        rects = ax.bar(
            x + offset,
            y,
            width,
            label=var.replace("_", " "),
            color=TI_COLORS[multiplier % len(TI_COLORS)],
            edgecolor=PLOT_EDGE_COLOR,
            linewidth=HISTOGRAM_LINE_WIDTH,
            bottom=bottom,
        )
        ax.bar_label(
            rects,
            padding=4,
            label_type="edge",
            fontsize=9,
            font=FONT_MED,
            color=PLOT_LABEL_COLOR,
        )
        multiplier += 1

    x_ticks = x - (width / 2) + (width * len(variables) / 2)

    ax.set_xticks(x_ticks, categories)
    ax.legend(loc="upper left", ncols=4)
    ax.set_ylim(0, max_value + max_value * BAR_Y_EMPTY_PERCENT)
    style_plot(ax, fig, title, x_label, y_label, size=size)
    plt.show()
