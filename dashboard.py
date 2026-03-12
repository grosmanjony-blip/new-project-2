import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

# Sample data for a simple dashboard
df = pd.DataFrame({
    "Category": ["A", "B", "C", "D"],
    "Value": [10, 20, 30, 40]
})

# Create a basic bar chart
fig = px.bar(df, x="Category", y="Value", title="Yoni Sample Bar Chart")

# Create Dash app
app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Simple Dashboard Example'),

    html.Div(children='''
        A very small dashboard built with Dash and Plotly.
    '''),

    dcc.Graph(
        id='example-bar-chart',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)