#! /usr/bin/env python
import numpy as np, pylab as plt

k_b = 1.380658e-16

def Tsky(nu):
    Tcmb = 2.73
    return 283.2 * (nu / 150e6)**(-2.47) + Tcmb

def sense(nu, N=352, B=100e6, t=3600, diam=14., Trx=260):
    A_eff = 0.7 * np.pi * (diam/2.)**2
    uJy_scalar = 2 * 1.22**2 * np.pi / (4 *np.log(2)) *  k_b / A_eff * 1e6 # uJy
    Tsys = Tsky(nu) + Trx
    nbls = N * (N-1) / 2
    return uJy_scalar * Tsys / np.sqrt(2 * B * t * nbls)

dnu = 1.
nu = np.arange(50.,250,dnu)
noise_uJy = sense(nu,B=dnu)
wgt = 1./ noise_uJy**2
print np.sqrt(np.sum((noise_uJy*wgt)**2)) / wgt.sum()
plt.plot(nu, sense(nu, B=dnu))
plt.show()
