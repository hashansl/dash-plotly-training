# import pandas as pd
# import plotly.express as px
import dash
import dash_html_components as html

app = dash.Dash(__name__)

#Import and clean data here



# ------------------------------------------------------------------------------
# App layout

app.layout = html.Div([])




# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components

@app.callback()



# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)