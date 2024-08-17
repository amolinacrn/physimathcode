# -*- coding: utf-8 -*-

import numpy as np
from iminuit import Minuit
from matplotlib import pyplot as plt
import matplotlib

from probfit import Chi2Regression, linear

# matplotlib.rcParams["text.usetex"] = True


xdat = np.loadtxt("dats.txt")
ndts = len(xdat[:, 0])
x = np.array(xdat[:, 0], dtype=float)
y = np.array(xdat[:, 1], dtype=float)
dy = np.array(xdat[:, 3], dtype=float)

x2r = Chi2Regression(linear, x, y, dy)

ajustar = Minuit(x2r, m=1, c=2)

fig, ax = plt.subplots()
ajustar.migrad()  # fit
x2r.draw(ajustar, ax=ax)
ax.grid()
plt.title("After")
plt.tight_layout()
plt.savefig("plotgraf.jpg")
plt.show()
