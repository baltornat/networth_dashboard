import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

mynw = pd.read_csv('./csv/mynetworth.csv', sep=',')

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Net worth Dashboard'),
    dcc.Dropdown(id='year-dropdown',
        options=[{'label': i, 'value': i}
            for i in mynw['Year'].unique()]),
    dcc.Graph(id='expenses-graph')
])

@app.callback(
    Output(component_id='expenses-graph', component_property='figure'),
    Input(component_id='year-dropdown', component_property='value')
)
def update_graph(selected_year):
    filtered_networth = mynw[mynw['Year'] == selected_year]
    line_fig = px.line(filtered_networth,
        x='Day', y='Expenses',
        title=f'Expenses in {selected_year}')
    return line_fig
    
if __name__ == '__main__':
    app.run_server(debug=True)
    
