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

In addition to installing Git locally, we will be using [GitHub](https://github.com/ "GitHub · Build software better, together.") to remotely store and share our code and documents. If you do not already have a GitHub account of your own, you can [request an educational account](https://github.com/edu) that will allow you to create private repositories that you can use for your course work.

## Python

The first step is to install Python on your computer. I will be teaching this course based on **Python 3.5**. Perhaps the easiest way to get a feature-complete version of Python on your system is to install the [Anaconda](http://continuum.io/downloads.html) distribution by Continuum Analytics. Anaconda is a completely free Python environment that includes includes almost 200 of the best Python packages for science and data analysis. Its simply a matter of downloading the installer (either graphical or command line), and running it on your system.

Be sure to download the Python 3.5 installer, by following the **Python 3.5 link**

![get Python 3](images/getpy3.png)

In addition to Python itself, we will be making use of several packages in the scientific stack. These include the following:

* [NumPy](http://www.numpy.org/ "NumPy &mdash; Numpy")
* [SciPy](http://www.scipy.org/ "SciPy.org &mdash; SciPy.org")
* [IPython](http://ipython.org/ "Announcements &mdash; IPython")
* [Pandas](http://pandas.pydata.org/ "Python Data Analysis Library &mdash; pandas: Python Data Analysis Library")
* [Matplotlib](http://matplotlib.org/ "matplotlib: python plotting &mdash; Matplotlib 1.2.1 documentation")
* [PyMC3](https://github.com/pymc-devs/pymc3 "pymc-devs/pymc3 · GitHub")
* [scikit-learn](http://scikit-learn.org/ "scikit-learn: machine learning in Python &mdash; scikit-learn 0.13.1 documentation")

We will install everything you require for Bios 8366 in one operation, described in the next section.

## Getting this repository

    git clone https://github.com/fonnesbeck/Bios8366.git

If you are not familiar with Git and GitHub, you can simply download the zip file of the repository at the top of the main repository page.

Then, move to the directory created by the clone/zip file:

    cd Bios8366

and install everything using `conda`:

    conda config --add channels conda-forge
    conda env create -f environment.yml
    
This will create an **environment** called `bios8366` that includes the packages required for the course.    
    
If you are not using the Anaconda Python distribution, you will need to manually install the packages listed in `environment.yml` using `pip`.

Which you probably don't want to do.

So install Anaconda.

To use the environment, you may type:

    source activate bios8366


## Document Preparation Tools

For preparing assignments and final projects, students may select from a variety of document preparation tools. Each of these facilitate scientific reporting by being able to embed code and typeset mathematical equations.

* [IPython Notebook](http://ipython.org/notebook.html "The IPython Notebook &mdash; IPython") A web-based interactive computational environment where you can combine code execution, text, mathematics, plots and rich media into a single document (recommended format)
* [LaTeX](http://www.latex-project.org) A scientific document preparation system.
* [pweave](http://mpastell.com/pweave/ "About Pweave &mdash; Pweave - reports from data with Python") A tool for embedding Python code and output in LaTeX, analogous to Sweave.
* [Pandoc](http://johnmacfarlane.net/pandoc/ "Pandoc - About pandoc") A tool for converting among markup formats.
* [Multimarkdown](http://fletcherpenney.net/multimarkdown/ "MultiMarkdown") An enhanced version of Markdown.
* [reStructuredText](http://docutils.sourceforge.net/rst.html "reStructuredText") An easy-to-read, what-you-see-is-what-you-get plaintext markup syntax and parser system

***The use of traditional word processing software, such as Microsoft Word or OpenOffice is not permitted in Bios 8366.***
