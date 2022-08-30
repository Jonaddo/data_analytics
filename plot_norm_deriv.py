#!/usr/bin/env python
# coding: utf-8



import numpy as np
import matplotlib.pyplot as plt



class NormPlot:
    """
    Plot the normal distribution and it's derivatives on one figure and saves it.


    Parameters
    ----------
    mu: float, default 0.0
        mean of the normal distribution
    sigma: float, default 1.0
        standard deviation of the normal distribution
    n_deriv: integer, default 1
        number of derivates to compute
    resolution: integer, default 100
        number of data points
    abscissa_lim: integer, default 5
        'width' of the plot


    History
    -------
        *06/2022 <jonathan.addo@hotmail.com>: Creation

    """
    def __init__(self, mu=0.0, sigma=1.0, n_deriv=1, resolution=100, abscissa_lim=5):
        self.mu = mu
        self.sigma = sigma
        self.n_deriv = n_deriv
        self.resolution = resolution
        self.abscissa_lim = abscissa_lim


    def normal_dist(self):
        self.norm_x = np.linspace(self.abscissa_lim*(-1), self.abscissa_lim, self.resolution)
        coef = 1/((2*np.pi*self.sigma**2)**0.5)
        exp_arg = -((self.norm_x-self.mu)**2)/(2*self.sigma**2)
        self.norm_y = coef*np.exp(exp_arg)


    def plot_derivatives(self, n=1):
        def plot_deriv(x, y, n):
            coord = list(zip(x, y))
            deriv = []
            for i in range(len(coord)):
                try:
                    x_dist = coord[i+1][0] - coord[i][0]
                    y_dist = coord[i+1][1] - coord[i][1]
                    slope = y_dist/x_dist
                    deriv.append(slope)
                except (IndexError, TypeError) as e:
                    deriv.append(None)
            if n < 1:
                raise TypeError("Only positive integers are allowed")
            elif n == 1:
                plt.plot(x, deriv)
            else:
                plt.plot(x, deriv)

                n -= 1
                plot_deriv(x, deriv, n)
        plt.plot(self.norm_x, self.norm_y)
        plot_deriv(self.norm_x, self.norm_y, n)
        plt.title(f'N({self.mu}, {self.sigma}) and first {n+1} derivatives')
        plt.savefig('normal_deriv.png', dpi=300, facecolor='lightgrey')
        plt.show()



if __name__ == '__main__':
    pn = NormPlot()
    # Generate the initial normal distribution y coordinates
    pn.normal_dist()
    # Plot the derivatives
    pn.plot_derivatives(3)


