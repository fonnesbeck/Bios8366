---

layout: default
title: Advanced Statistical Computing

---

# Software

Bios 8366 is taught using Python and the *Scientific Stack*, a set of core scientific computing packages written and maintained by various third parties.

## Git

The use of version control systems is essential for effective scientific computing. In Bios 8366, we [make extensive use of Git](http://fonnesbeck.github.io/Bios8366/git.html), which is one of several widely-used versioning systems.

To install Git, you can either download an installer from [the Git website](http://git-scm.com), or if you are on a UNIX-based computer, install it via your system's package manager (recommended). On Mac OS X, you can easily install a variety of software packages using [Homebrew](http://mxcl.github.io/homebrew/ "Homebrew — MacPorts driving you to drink? Try Homebrew!"). To obtain Git, simply type:

    brew install git

On Linux, you can issue a similar command with `apt-get` or `yum`, depending on which Linux distribution you are using.

Git can also be installed using the `conda` tool described below.

In addition to installing Git locally, we will be using [GitHub](https://github.com/ "GitHub · Build software better, together.") to remotely store and share our code and documents. If you do not already have a GitHub account of your own, you can [request an educational account](https://github.com/edu) that will allow you to create private repositories that you can use for your course work.

On Windows, the [Chocolatey](https://chocolatey.org/) package manager can be used to install git and other relevant software. 

    choco install git

However, I recommend using Windows Subsystem for Linux (WSL2) for serious development and data science on Windows. This allows you to run Linux seamlessly from Windows, which helps avoid many of the problems that can crop up when using Python on Windows.


## Python

The first step is to install Python on your computer. I will be teaching this course based on **Python 3.9**. Perhaps the easiest way to get a feature-complete version of Python on your system is to install the [Anaconda](http://www.anaconda.com/download) distribution. Anaconda is a completely free Python environment that includes most of the important Python packages for science and data analysis. Its simply a matter of downloading the installer (either graphical or command line), and running it on your system.

An even better alternative is to use the [Miniforge](https://github.com/conda-forge/miniforge) system, which is a community-led project that provides the core subset of the Anaconda system, and is tied to the [CondaForge](https://conda-forge.org/ "CondaForge — The community-driven conda repository.") repository for downloading the most current versions of scientific Python packages.

You can download the installer for your system from the [Miniforge GitHUb repository](https://github.com/conda-forge/miniforge#download).

In addition to Python itself, we will be making use of several packages in the scientific stack. These include the following:

* [NumPy](http://www.numpy.org/ "NumPy &mdash; Numpy")
* [SciPy](http://www.scipy.org/ "SciPy.org &mdash; SciPy.org")
* [Jupyter](http://jupyter.org/ "Jupyter")
* [Pandas](http://pandas.pydata.org/ "Python Data Analysis Library &mdash; pandas: Python Data Analysis Library")
* [Matplotlib](http://matplotlib.org/ "matplotlib: python plotting &mdash; Matplotlib 1.2.1 documentation")
* [PyMC](https://github.com/pymc-devs/pymc "pymc-devs/pymc · GitHub")
* [scikit-learn](http://scikit-learn.org/ "scikit-learn: machine learning in Python &mdash; scikit-learn documentation")

We will install everything you require for Bios 8366 in one operation, described in the next section.

## Getting this repository

    git clone https://github.com/fonnesbeck/Bios8366.git

If you are not familiar with Git and GitHub, you can simply download the zip file of the repository at the top of the main repository page.

Then, move to the directory created by the clone/zip file:

    cd Bios8366

and install everything using `conda`:

    conda env create -f environment.yml
    
This will create an **environment** called `bios8366` that includes the packages required for the course.    
    
If you are not using the Miniforge or Anaconda, you will need to manually install the packages listed in `environment.yml` using `pip`.

Which you probably don't want to do.

So install Miniforge.

To use the environment, you may type:

    conda activate bios8366


## Document Preparation Tools

For preparing assignments and final projects, students may select from a variety of document preparation tools. Each of these facilitate scientific reporting by being able to embed code and typeset mathematical equations.

* [Jupyter Notebook](http://jupyter.org) A web-based interactive computational environment where you can combine code execution, text, mathematics, plots and rich media into a single document (recommended format)
* [LaTeX](http://www.latex-project.org) A scientific document preparation system.
* [pweave](http://mpastell.com/pweave/ "About Pweave &mdash; Pweave - reports from data with Python") A tool for embedding Python code and output in LaTeX, analogous to Sweave.
* [Pandoc](http://johnmacfarlane.net/pandoc/ "Pandoc - About pandoc") A tool for converting among markup formats.
* [reStructuredText](http://docutils.sourceforge.net/rst.html "reStructuredText") An easy-to-read, what-you-see-is-what-you-get plaintext markup syntax and parser system

***The use of traditional word processing software, such as Microsoft Word or OpenOffice is not permitted in Bios 8366.***
