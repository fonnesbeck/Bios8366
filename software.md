---

layout: default
title: Advanced Statistical Computing

---

# Software

Bios 366 is taught using Python and the "Scientific Stack", a set of core scientific computing packages written and maintained by various third parties.

## Python

The first step is to install Python on your computer. I will be teaching this course based on **Python 2.7.2**. If you are running Mac OS X, Python is already included in the operating system that is shipped with the computer. I recommend that you upgrade to OS X 10.8 (Mountain Lion) if possible, so that you are running a relatively recent version of Python.

If you are running Windows or Linux, you may not already have Python installed (though it is installed by default on many Linux distributions). If Python is not on your system, you can either download an installer from [Python.org](http://python.org) or install a third-party distribution (see below). I recommend the latter, since these distributions are enhanced, containing most or all of the packages required for the course.

In addition to Python itself, we will be making use of several packages in the scientific stack. These include the following:

* [NumPy](http://www.numpy.org/ "NumPy &mdash; Numpy")
* [SciPy](http://www.scipy.org/ "SciPy.org &mdash; SciPy.org")
* [IPython](http://ipython.org/ "Announcements &mdash; IPython")
* [Pandas](http://pandas.pydata.org/ "Python Data Analysis Library &mdash; pandas: Python Data Analysis Library")
* [Matplotlib](http://matplotlib.org/ "matplotlib: python plotting &mdash; Matplotlib 1.2.1 documentation")
* [PyMC](https://github.com/pymc-devs/pymc "pymc-devs/pymc · GitHub")
* [scikit-learn](http://scikit-learn.org/ "scikit-learn: machine learning in Python &mdash; scikit-learn 0.13.1 documentation")

If your Python distribution does not include these packages, you can install them using either `pip` or `easy_install`.

## All-in-one Scientific Python

There are a handful of enhanced Python distributions that include easy installers and all of the packages required for this course.

* [Anaconda](http://continuum.io/downloads.html) by Continuum Analytics. Completely free enterprise-ready Python distribution for large-scale data processing, predictive analytics, and scientific computing
* [Enthought Canopy](https://www.enthought.com/products/canopy/) Enthought Canopy is a comprehensive Python analysis environment with easy installation & updates of the proven Enthought Python distribution.

These are the most widely-used distributions for scientific computing in Python. Alternatives include [Pyzo](http://www.pyzo.org/), [WinPython](http://code.google.com/p/winpython/) and [Python(x,y)](http://code.google.com/p/pythonxy/).

## Mac OS X

Since OS X ships with Python pre-installed, it is often inconvenient to install another Python distribution. For users running OS X 10.8 (Mountain Lion), I build and maintain the [Scipy Superpack](http://fonnesbeck.github.io/ScipySuperpack/) which are recent builds of fundamental Python scientific computing packages for OS X. The installer is a simple shell script that will install recent 64-bit builds of Numpy,  Scipy, Matplotlib, IPython, Pandas, Statsmodels, Scikit-Learn and PyMC.

## Linux

Users on Linux can quickly install the necessary packages from repositories.

### Ubuntu & Debian

    sudo apt-get install python-numpy python-scipy python-matplotlib \
    ipython ipython-notebook python-pandas python-sympy python-nose

The versions in Ubuntu 12.10 and Debian 7.0 meet the current Scipy stack specification. Users might also want to add the [NeuroDebian](http://neuro.debian.net/) repository for extra Scipy packages.

### Fedora

    sudo yum install numpy scipy python-matplotlib ipython python-pandas \
    sympy python-nose

Users of Fedora 17 and earlier should then upgrade IPython using pip:

    sudo pip install --upgrade ipython

## Git

The use of version control systems is essential for effective scientific computing. In Bios 366, we [make extensive use of Git](http://fonnesbeck.github.io/Bios366/git.html), which is one of several widely-used versioning systems.

To install Git, you can either download an installer from [the Git website](http://git-scm.com), or if you are on a UNIX-based computer, install it via your system's package manager (recommended). On Mac OS X, you can easily install a variety of software packages using [Homebrew](http://mxcl.github.io/homebrew/ "Homebrew — MacPorts driving you to drink? Try Homebrew!"). To obtain Git, simply type:

    brew install git

On Linux, you can issue a similar command with `apt-get` or `yum`, depending on which Linux distribution you are using.

In addition to installing Git locally, we will be using [GitHub](https://github.com/ "GitHub · Build software better, together.") to remotely store and share our code and documents. If you do not already have a GitHub account of your own, you can [request an educational account](https://github.com/edu) that will allow you to create private repositories that you can use for your course work.


## Document Preparation Tools

For preparing assignments and final projects, students may select from a variety of document preparation tools. Each of these facilitate scientific reporting by being able to embed code and typeset mathematical equations.

* [IPython Notebook](http://ipython.org/notebook.html "The IPython Notebook &mdash; IPython") A web-based interactive computational environment where you can combine code execution, text, mathematics, plots and rich media into a single document
* [LaTeX](http://www.latex-project.org) A scientific document preparation system.
    - [pweave](http://mpastell.com/pweave/ "About Pweave &mdash; Pweave - reports from data with Python") A tool for embedding Python code and output in LaTeX, analogous to Sweave.
    - [Pandoc](http://johnmacfarlane.net/pandoc/ "Pandoc - About pandoc") A tool for converting among markup formats.
* [Multimarkdown](http://fletcherpenney.net/multimarkdown/ "MultiMarkdown") An enhanced version of Markdown.
* [reStructuredText](http://docutils.sourceforge.net/rst.html "reStructuredText") An easy-to-read, what-you-see-is-what-you-get plaintext markup syntax and parser system

The use of traditional word processing software, such as Microsoft Word or OpenOffice is not permitted in Bios 366.
