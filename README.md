## COVID-19 Notebooks

The notebooks in this repo let you examine and plot the data shared through
the JHU CSSE git repo, at https://github.com/CSSEGISandData/COVID-19

The git repo provides country-by-country (and province by province, for some
countries) daily stats for confirmed COVID-19 cases, deaths, and recoveries.
Some of the data is provided in time-series CSV files, but the more granular
data (down to county level, in the US) is in daily CSV reports.  The code
here shows how to dig out the data from these files in a form that makes it
easy to plot the country-level or US state-level data.

### Installation

The scripts in this repo were generated from the original notebooks using
[Jupytext](https://github.com/mwouts/jupytext), a Jupyter extension that
makes it easy to work with the same notebooks both as notebooks, which don't
play well with version control, and as text files.

What are checked in here are the Python-script versions of the notebooks.
To use these in Jupyter, you will need to have the Jupytext extension
installed; this will regenerate the original notebook when you load the .py
files provided here.

Sorry for this extra step - I'm still trying to settle on the best way to
share Jupyter notebooks via Github, and this is an experiment for me.

### Usage
1. To use these notebooks you need to have the data repo checked out.  You
can do that with the command,

    git clone https://github.com/CSSEGISandData/COVID-19.git

2. Each of the notebooks requires you to specify the location of the repo,
where you checked it out, near the beginning of the notebook.

Once these things are done, you can execute the notebooks and look at the
data in different ways.


