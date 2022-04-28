# python-flask-app-plotly

https://towardsdatascience.com/web-visualization-with-plotly-and-flask-3660abf9c946

## 2 important files:
app.py
index.html

## app.py
this file initializes a flask app, then defines a python function that: generates the plotly chart, encodes the chart in JSON, then renders index.html with the JSON-encoded chart

## index.html
this file creates an object to hold the plotly chart, and contains a script to receive the JSON-encoded chart and insert it into the object
