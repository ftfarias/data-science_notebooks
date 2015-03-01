# -*- encoding: utf-8 -*-

import scipy as sp
import matplotlib.pyplot as plt

colors = ['g', 'k', 'b', 'r']
linestyles = ['-', '-.', '--', ':', '-']

def plot_models(x, y, models, mx=None, ymax=None, xmin=None):
    plt.clf()
    plt.scatter(x, y, s=10, alpha=0.3)
    plt.title("Tráfego no último mês".decode('utf-8'))
    plt.xlabel("Tempo")
    plt.ylabel("Hits/Hora")
    plt.xticks([w * 7 * 24 for w in range(10)], ['week %i' % w for w in range(10)])
    if models:
        if mx is None:
            mx = sp.linspace(0, x[-1], 1000)
        for model, style, color in zip(models, linestyles, colors):
            plt.plot(mx, model(mx), linestyle=style, linewidth=2, c=color)
        plt.legend(["d=%i" % m.order for m in models], loc="upper left")
        plt.autoscale(tight=True)
        plt.ylim(ymin=0)
        if ymax:
            plt.ylim(ymax=ymax)
        if xmin:
            plt.xlim(xmin=xmin)
        plt.grid(True, linestyle='-', color='0.75')
        plt.show()
