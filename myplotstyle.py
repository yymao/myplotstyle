"""
My personal plot style
Project website: https://github.com/yymao/myplotstyle
Copyright (c) 2023-2024 Yao-Yuan Mao (yymao)
"""

import cmasher
import cmcrameri
import matplotlib.pyplot

cmr = cmasher
cmc = cmcrameri.cm
plt = matplotlib.pyplot

__all__ = ["plt", "cmr", "cmc", "FIG_WIDTH", "FIG_HEIGHT", "FIG_WIDTH_WIDE", "get_figsize", "legend_ordered"]
__version__ = "1.1.1"

_margin = 0.22
_width = 5.8
_width_wide = (_width - _margin) / 3.35 * 7.1 + _margin


def get_figsize(wide=False, ratio=1.35):
    width = _width_wide if wide else _width
    height = (width - _margin) / ratio + _margin
    return (round(width, 2), round(height, 2))


FIG_WIDTH, FIG_HEIGHT = get_figsize()
FIG_WIDTH_WIDE = get_figsize(wide=True)[0]

plt.rcParams.update({
    "figure.constrained_layout.use": True,
    "figure.dpi": 200,
    "figure.figsize": (FIG_WIDTH, FIG_HEIGHT),
    "mathtext.fontset": "stix",
    "font.family": "STIXGeneral",
    "font.size": 15,
    "axes.labelsize": 16,
    "legend.frameon": False,
    "legend.handletextpad": 0.5,
    "lines.markersize": 5,
    "xtick.minor.visible": True,
    "ytick.minor.visible": True,
    "xtick.major.size": 7,
    "xtick.minor.size": 4,
    "ytick.major.size": 7,
    "ytick.minor.size": 4,
    "savefig.bbox": "tight",
    "savefig.dpi": 200,
})


def legend_ordered(axes=None, order=None, **kwargs):
    if axes is None:
        axes = plt.gca()
    if order is None:
        if isinstance(axes, plt.Axes):
            return axes.legend(**kwargs)
        order = axes
        axes = plt.gca()
    handles, labels = axes.get_legend_handles_labels()
    handles_new = []
    labels_new = []
    for i in order:
        try:
            h = handles[i]
            l = labels[i]
        except IndexError:
            continue
        else:
            handles_new.append(h)
            labels_new.append(l)
    return axes.legend(handles_new, labels_new, **kwargs)
