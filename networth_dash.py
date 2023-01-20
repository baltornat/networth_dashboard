import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

mynw = pd.read_csv('./csv/mynetworth.csv', sep=',')

categories = [

]

years = [
    '2023'
]

### PRELIMINAR OPERATIONS ON THE DATAFRAME
# Convert the date to datetime64
mynw['Date'] = pd.to_datetime(mynw['Date'])
# Fill NaN with 0
mynw[['Incomings','Expenses']] = mynw[['Incomings','Expenses']].fillna(0)
# Create daily networth
mynw['Balance'] = (mynw['Incomings'] - mynw['Expenses']).cumsum()

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Net Worth Dashboard'),
    dcc.Dropdown(id='year-dropdown',
        options=[{'label': i, 'value': i}
            for i in years]),
    dcc.Graph(id='expenses-graph')
])

@app.callback(
    Output(component_id='expenses-graph', component_property='figure'),
    Input(component_id='year-dropdown', component_property='value')
)
def line_chart(selected_year):
    filtered_mynw = mynw[mynw['Date'].dt.strftime('%Y') == selected_year]
    line_fig = px.line(filtered_mynw, x='Date', y='Balance', title=f'Annual Trend ({selected_year})')
    return line_fig
    
if __name__ == '__main__':
    app.run_server(debug=True)
    
