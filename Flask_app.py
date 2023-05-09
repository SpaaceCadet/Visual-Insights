
from flask import Flask , render_template
import numpy as np
import plotly.graph_objs as go
import plotly.express as px


# Everything is in your current directory
app = Flask(__name__)
#Python decorator / add more functionality .
# where to go , if someone navigates to the website (yahya.com)
@app.route('/')
# we'll perform then a function
def index():

    return render_template("index.html")



if __name__ == '__main__':
    app.run()


