# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 10:06:21 2024

@author: samish
"""

import numpy as np
import matplotlib.pyplot as plt
from skimage import data, io

# Aquí comentario cambiado

imagen = io.imread(r'C:\Users\ikerf\Desktop\Upiita\7mo semestre\Patrones\Imagenes\objetos1.jpg')
# imagen = data.astronaut()
Parte=imagen[0:50,0:50,:]
plt.figure(0)
plt.imshow(imagen)
plt.figure(1)
plt.imshow(Parte)

hr = np.zeros(256) #histograma rojos
hv = np.zeros(256) #istograma verdes
ha = np.zeros(256)

filas = imagen.shape[0]
columnas = imagen.shape[1]
capas = imagen.shape[2]

# for i in range(0,filas,1):
#     for j in range(0,columnas,2):
#         posR = imagen
