import csv
import numpy as np

fname = 'Incidentes_georreferenciados_2019.txt'
a = np.loadtxt(fname, delimiter=',', skiprows=1)