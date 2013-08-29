
# Reproducible Research and Reporting with iPython Notebooks

## Reproducible Research

> reproducing conclusions from a single experiment based on the measurements
from that experiment

The most basic form of reproducibility is a complete description of the data and
associated analyses (including code!) so the results can be *exactly* reproduced
by others.

Reproducing calculations can be onerous, even with one's own work!

Scientific data are becoming larger and more complex, making simple descriptions
inadequate for reproducibility. As a result, most modern research is
irreproducible without tremendous effort.

*** Reproducible research is not yet part of the culture of science in general,
or scientific computing in particular. ***

## Scientific Computing Workflow

There are a number of steps to scientific endeavors that involve computing:

![workflow](http://f.cl.ly/items/3B0l063n2T0H1p041U3L/workflow.png)

Many of the standard tools impose barriers between one or more of these steps.
This can make it difficult to iterate, reproduce work.



## IPython

**IPython** is an enhanced Python shell which provides a more robust and
productive development environment for users.

It includes the **HTML notebook** featured here, as well as support for
**interactive data visualization** and easy high-performance **parallel
computing**.

In[2]:

```
def f(x):
    return (x-3)*(x-5)*(x-7)+85

import numpy as np
x = np.linspace(0, 10, 200)
y = f(x)
plot(x,y)
```




    [<matplotlib.lines.Line2D at 0x1150e4a50>]




[!image]()


If you type at the system prompt:

    $ ipython qtconsole

instead of opening in a terminal, IPython will start a graphical console that at
first sight appears just like a terminal, but which is in fact much more capable
than a text-only terminal.  This is a specialized terminal designed for
interactive scientific work, and it supports full multi-line editing with color
highlighting and graphical calltips for functions, it can keep multiple IPython
sessions open simultaneously in tabs, and when scripts run it can display the
figures inline directly in the work area.

![qtconsole](files/images/qtconsole.png)

## iPython Notebook

The HTML lets you document your workflow using either HTML or Markdown.

The IPython Notebook consists of two related components:

* A JSON based Notebook document format for recording and distributing Python
code and rich text.
* A web-based user interface for authoring and running notebook documents.

The Notebook can be used by starting the Notebook server with the command:

    $ ipython notebook

This initiates an **iPython engine**, which is a Python instance that takes
Python commands over a network connection. If we want to enable inline plotting
of figures via Matplotlib, we can add a `--pylab inline` flag to the command.

The **IPython controller** provides an interface for working with a set of
engines, to which one or more **iPython clients** can connect.

The Notebook gives you everything that a browser gives you. For example, you can
embed images, videos, or entire websites.

In[3]:

```
from IPython.display import HTML
HTML("<iframe src=http://fonnesbeck.github.io/Bios366 width=700 height=350></iframe>")
```






In[4]:

```
from IPython.display import YouTubeVideo
YouTubeVideo("BS4Wd5rwNwE")
```






### Remote Code

Use `%load` to add remote code

### Mathjax Support

Mathjax ia a javascript implementation of LaTeX that allows equations to be
embedded into HTML. For example, this markup:

    """$$ \int_{a}^{b} f(x)\, dx \approx \frac{1}{2} \sum_{k=1}^{N} \left( x_{k}
- x_{k-1} \right) \left( f(x_{k}) + f(x_{k-1}) \right). $$"""

becomes this:

$$
\int_{a}^{b} f(x)\, dx \approx \frac{1}{2} \sum_{k=1}^{N} \left( x_{k} - x_{k-1}
\right) \left( f(x_{k}) + f(x_{k-1}) \right).
$$

## SymPy Support

SymPy is a Python library for symbolic mathematics. It supports:

* polynomials
* calculus
* solving equations
* discrete math
* matrices

In[6]:

```
from sympy import *
%load_ext sympyprinting
x, y = symbols("x y")
```


    The sympyprinting extension is already loaded. To reload it, use:
      %reload_ext sympyprinting


In[7]:

```
eq = ((x+y)**2 * (x+1))
eq
```




[!image]()



In[8]:

```
expand(eq)
```




[!image]()



In[9]:

```
(1/cos(x)).series(x, 0, 6)
```




[!image]()



### Magic functions

IPython has a set of predefined ‘magic functions’ that you can call with a
command line style syntax. These include:

* `%run`
* `%edit`
* `%debug`
* `%timeit`
* `%paste`
* `%load_ext`



In[10]:

```
%lsmagic
```




    Available line magics:
    %alias  %alias_magic  %autocall  %automagic  %autosave  %bookmark  %cd  %clear  %colors  %config  %connect_info  %debug  %dhist  %dirs  %doctest_mode  %ed  %edit  %env  %gui  %hist  %history  %install_default_config  %install_ext  %install_profiles  %killbgscripts  %less  %load  %load_ext  %loadpy  %logoff  %logon  %logstart  %logstate  %logstop  %lsmagic  %macro  %magic  %man  %matplotlib  %more  %notebook  %page  %pastebin  %pdb  %pdef  %pdoc  %pfile  %pinfo  %pinfo2  %popd  %pprint  %precision  %profile  %prun  %psearch  %psource  %pushd  %pwd  %pycat  %pylab  %qtconsole  %quickref  %recall  %rehashx  %reload_ext  %rep  %rerun  %reset  %reset_selective  %run  %save  %sc  %store  %sx  %system  %tb  %time  %timeit  %unalias  %unload_ext  %who  %who_ls  %whos  %xdel  %xmode
    
    Available cell magics:
    %%!  %%HTML  %%SVG  %%bash  %%capture  %%debug  %%file  %%html  %%javascript  %%latex  %%perl  %%prun  %%pypy  %%python  %%python3  %%ruby  %%script  %%sh  %%svg  %%sx  %%system  %%time  %%timeit  %%writefile
    
    Automagic is ON, % prefix IS NOT needed for line magics.



Timing the execution of code; the `timeit` magic exists both in line and cell
form:

In[11]:

```
%timeit np.linalg.eigvals(np.random.rand(100,100))
```


    100 loops, best of 3: 8.42 ms per loop


In[12]:

```
%%timeit a = np.random.rand(100, 100)
np.linalg.eigvals(a)
```


    100 loops, best of 3: 8.12 ms per loop


IPython also creates aliases for a few common interpreters, such as bash, ruby,
perl, etc.

These are all equivalent to `%%script <name>`

In[13]:

```
%%ruby
puts "Hello from Ruby #{RUBY_VERSION}"
```


    Hello from Ruby 1.8.7


In[14]:

```
%%bash
echo "hello from $BASH"
```


    hello from /bin/bash


IPython has an `rmagic` extension that contains a some magic functions for
working with R via rpy2. This extension can be loaded using the `%load_ext`
magic as follows:

In[15]:

```
%load_ext rmagic
```

In[16]:

```
x,y = arange(10), random.normal(size=10)
```

In[17]:

```
%%R -i x,y -o XYcoef
lm.fit <- lm(y~x)
par(mfrow=c(2,2))
print(summary(lm.fit))
plot(lm.fit)
XYcoef <- coef(lm.fit)
```



    
    Call:
    lm(formula = y ~ x)
    
    Residuals:
         Min       1Q   Median       3Q      Max 
    -2.37075 -0.60668 -0.02019  0.54861  1.89539 
    
    Coefficients:
                Estimate Std. Error t value Pr(>|t|)
    (Intercept)  0.16783    0.81415   0.206    0.842
    x           -0.02431    0.15250  -0.159    0.877
    
    Residual standard error: 1.385 on 8 degrees of freedom
    Multiple R-squared:  0.003166,	Adjusted R-squared:  -0.1214 
    F-statistic: 0.02541 on 1 and 8 DF,  p-value: 0.8773
    




[!image]()


In[18]:

```
XYcoef
```




    [ 0.16782713 -0.02430967]



## Exporting and Converting Notebooks

In IPython 1.0, one can convert an `.ipynb` notebook document file into various
static formats via the `nbconvert` tool. Currently, nbconvert is a command line
tool, run as a script using IPython.

In[ ]:

```
!ipython nbconvert --to
```

## Parallel iPython

Before running the next cell, make sure you have first started your cluster, you
can use the [clusters tab in the dashboard](/#tab2) to do so.

In[18]:

```
from IPython.parallel import Client
client = Client()
dv = client.direct_view()
```

In[19]:

```
len(dv)
```




[!image]()



In[20]:

```
def where_am_i():
    import os
    import socket
    
    return "In process with pid {0} on host: '{1}'".format(
        os.getpid(), socket.gethostname())
```

In[21]:

```
where_am_i_direct_results = dv.apply(where_am_i)
where_am_i_direct_results.get()
```




    [In process with pid 79873 on host: 'Cepeda.local',
     In process with pid 79874 on host: 'Cepeda.local',
     In process with pid 79875 on host: 'Cepeda.local']



## Links and References

[IPython Notebook Viewer](http://nbviewer.ipython.org) Displays static HTML
versions of notebooks, and includes a gallery of notebook examples.

[NotebookCloud](https://notebookcloud.appspot.com) A service that allows you to
launch and control IPython Notebook servers on Amazon EC2 from your browser.

[A Reference-Free Algorithm for Computational Normalization of Shotgun
Sequencing Data](http://ged.msu.edu/papers/2012-diginorm/) A landmark example of
reproducible research in genomics: Git repo, iPython notebook, data and scripts.

---

In[1]:

```
from IPython.core.display import HTML
def css_styling():
    styles = open("styles/custom.css", "r").read()
    return HTML(styles)
css_styling()
```





