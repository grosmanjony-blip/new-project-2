import plotly.express as px

# Example data for oil prices
oil_data = {
    "Date": ["2024-01", "2024-02", "2024-03", "2024-04", "2024-05"],
    "Oil Price (USD/barrel)": [78, 82, 80, 85, 88]
}

import pandas as pd
df_oil = pd.DataFrame(oil_data)

# Create a simple line chart for oil price
fig_oil = px.line(df_oil, x="Date", y="Oil Price (USD/barrel)", title="Example Oil Price Chart")

# Show the chart (for usage in a script; in e.g., Jupyter, use fig_oil.show())
fig_oil.show()
