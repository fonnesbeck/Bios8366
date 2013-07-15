---

layout: default
title: Advanced Statistical Computing

---

# Software

Bios 366 is taught using Python and the "Scientific Stack", a set of core scientific computing packages written and maintained by various third parties.

There are a handful of enhanced Python distributions that include easy installers and all of the packages required for this course.

* [Anaconda](http://continuum.io/downloads.html) by Continuum Analytics. Completely free enterprise-ready Python distribution for large-scale data processing, predictive analytics, and scientific computing
* [Enthought Canopy](https://www.enthought.com/products/canopy/) Enthought Canopy is a comprehensive Python analysis environment with easy installation & updates of the proven Enthought Python distribution.

These are the most widely-used distributions for scientific computing in Python. Alternatives include [Pyzo](http://www.pyzo.org/), [WinPython](http://code.google.com/p/winpython/) and [Python(x,y)](http://code.google.com/p/pythonxy/).

## Mac OS X

Since OS X ships with Python pre-installed, it is often inconvenient to install another Python distribution. For users running OS X 10.8 (Mountain Lion), I build and maintain the [Scipy Superpack](http://fonnesbeck.github.io/ScipySuperpack/) which are recent builds of fundamental Python scientific computing packages for OS X. The installer is a simple shell script that will install recent 64-bit builds of Numpy,  Scipy, Matplotlib, IPython, Pandas, Statsmodels, Scikit-Learn and PyMC.

## Linux

Users on Linux can quickly install the necessary packages from repositories.

### Ubuntu & Debian

    sudo apt-get install python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose

The versions in Ubuntu 12.10 and Debian 7.0 meet the current Scipy stack specification. Users might also want to add the [NeuroDebian](http://neuro.debian.net/) repository for extra Scipy packages.

### Fedora

    sudo yum install numpy scipy python-matplotlib ipython python-pandas sympy python-nose

Users of Fedora 17 and earlier should then upgrade IPython using pip:

    sudo pip install --upgrade ipython