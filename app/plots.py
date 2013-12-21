__author__ = 'rebecca'

from bokeh.plotting import *

import numpy as np


# Define a function that will return an HTML snippet.
def build_plot():

    # Set the output for our plot.

    output_file('plot.html', title='Plot')

    # Create some data for our plot.

    x_data = np.arange(1, 101)
    y_data = np.random.randint(0, 101, 100)

    # Create a line plot from our data.

    line(x_data, y_data)

    # Create an HTML snippet of our plot.

    snippet = curplot().create_html_snippet(embed_base_url='../static/js/',
                                            embed_save_loc='./static/js')

    # Return the snippet we want to place in our page.

    return snippet