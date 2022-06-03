# SSA-Name-Data


This provides a set of functions in Python to process and visualize raw Social Security Adminsitration name data, accessible from the [SSA's website](https://www.ssa.gov/oact/babynames/limits.html). Currently, functions only work with the National data, which you should download as a zip and drop in the working directory after you clone


## Getting set up
You should use a virtual environment! I use conda. You can configure a conda env using the included `requirements.txt` or `environment.yml` as follows:

`conda create --name <env_name> --file requirements.txt`


## Functions
All functions are stored in `functions.py`. The key ones:
- `fileReader()` loads in all available files and creates a single pandas df. 
- `NameSelector()` takes in a list of names, beginning and end years, and sex to create a single dataframe that shows each name's popularity over time
- `nameGraph()` takes the same arguments as `NameSelector()`, and creates a plotly line graph of the count of each name over time. The graph will open up in your browser. 



