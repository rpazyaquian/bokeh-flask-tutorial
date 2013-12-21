__author__ = 'rebecca'

from flask import Flask, render_template
from plots import build_plot

app = Flask(__name__)

# Define our URLs and pages.
@app.route('/')
def render_plot():
    plot_snippet = build_plot()

    return render_template('plots.html', snippet=plot_snippet)

if __name__ == '__main__':
    app.run(debug=True)