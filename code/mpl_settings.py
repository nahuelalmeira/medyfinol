from __future__ import print_function
from __future__ import unicode_literals

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', 
          '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', 'k', 'y',
          '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', 
          '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', 'k', 'y']
markers = ['s', 'o', 'v', 'D', '*', '<', '>', 'H', 'p', 'P', '^',
           's', 'o', 'v', 'D', '*', '<', '>', 'H', 'p', 'P', '^',
           's', 'o', 'v', 'D', '*', '<', '>', 'H', 'p', 'P', '^',
           's', 'o', 'v', 'D', '*', '<', '>', 'H', 'p', 'P', '^']

import os
import numpy as np
import matplotlib.pyplot as plt

import matplotlib as mpl

rc_font_size = 30
rc_label_size = 28
rc_legend_size = 26
mpl.rcParams['figure.figsize'] = (12, 8)

mpl.rcParams['axes.titlesize'] = rc_legend_size

mpl.rcParams['text.usetex'] = True
mpl.rcParams['text.latex.unicode'] = True
mpl.rcParams['text.latex.preamble'] = [r'\boldmath']
mpl.rcParams['lines.linewidth'] = 3
mpl.rcParams['legend.fontsize'] = rc_legend_size
mpl.rcParams['savefig.transparent'] = True
mpl.rcParams['savefig.bbox'] = 'tight'
mpl.rcParams['axes.linewidth'] = 3
mpl.rcParams['axes.labelsize'] = rc_font_size
mpl.rcParams['xtick.labelsize'] = rc_label_size
mpl.rcParams['ytick.labelsize'] = rc_label_size

mpl.rcParams['xtick.major.width'] = 4
mpl.rcParams['xtick.major.size'] = 10
mpl.rcParams['xtick.minor.visible'] = True
mpl.rcParams['xtick.minor.width'] = 3
mpl.rcParams['xtick.minor.size'] = 5

mpl.rcParams['ytick.major.width'] = 4
mpl.rcParams['ytick.major.size'] = 10
mpl.rcParams['ytick.minor.visible'] = True
mpl.rcParams['ytick.minor.width'] = 3
mpl.rcParams['ytick.minor.size'] = 5

mpl.rcParams['patch.linewidth'] = 1.5

def test1(savefig=False):

    x = np.linspace(0, 5, 100)
    y = np.sin(x)

    plt.figure()
    plt.xlabel("$x$")
    plt.ylabel("$\mathrm{sin}\,(x)$")
    plt.plot(x, y, label="$\mathrm{Trigonometric\;function}")
    plt.plot(x, y+1, label="Trigonometric function 2")
    plt.legend(loc="best")
    if savefig:
        plt.savefig("test1.pdf")
    else:
        plt.show()

if __name__ == '__main__':

    print(os.getcwd())
    test1()
    test1(savefig=True)
