import random
import matplotlib.ticker as mticker
from .models import *
import numpy as np
from iminuit import Minuit
from matplotlib import pyplot as plt
import matplotlib
from .utils_pdf import render_pdf_view

matplotlib.rcParams["text.usetex"] = True
from probfit import Chi2Regression, linear
