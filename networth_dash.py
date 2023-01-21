import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Import CSV. Structure: Date/Incomings/Expenses/Categories/Notes
mynw = pd.read_csv('./csv/mynetworth.csv', sep=',')

categories = ['Clothes', 'Food', 'Other', 'Amazon', 'Bar', 'Gas', 'Medicines', 'Home', 'Friends', 'Presents', 'Technology', 'Phone', 'Transport', 'Vacation']
years = ['2023']

### PRELIMINAR OPERATIONS ON THE DATAFRAME
# Convert date to datetime64
mynw['Date'] = pd.to_datetime(mynw['Date'])
# Fill NaN in Incomings and Expenses with 0
mynw[['Incomings','Expenses']] = mynw[['Incomings','Expenses']].fillna(0)
# Default category if not set is 'Other'
mynw['Categories'] = mynw['Categories'].where(mynw['Categories'].isin(categories), other='Other')
# Create daily balance in a new column named 'Balance'
mynw['Balance'] = (mynw['Incomings'] - mynw['Expenses']).cumsum()

app = dash.Dash(
    __name__,
    external_stylesheets=['./assets/style.css', dbc.themes.SANDSTONE],
    suppress_callback_exceptions=True
)

app.layout = html.Div(children=[
    html.H1(children='Net Worth Dashboard'),
    dbc.Row([
        dcc.Dropdown(id='year-dropdown', options=[{'label': i, 'value': i} for i in years]),
    ], className='mb-4'),
    dbc.Row([
        dbc.Col(
            dcc.Graph(id='annual-trend-graph'),
            md=6
        ),
        dbc.Col(
            dcc.Graph(id='expenses-by-category-graph'),
            md=6
        )
    ], className='mb-4'),
    dbc.Row([
        html.H1(f"Total incomings: {mynw['Incomings'].sum()}€"),
        html.H1(f"Total expenses: {mynw['Expenses'].sum()}€")
    ], className='mb-4'),
], style={'background-color': '#C7BEC7',
          'width': 'auto',
          'padding': '25px'})

# Annual Trend
@app.callback(
    Output(component_id='annual-trend-graph', component_property='figure'),
    Input(component_id='year-dropdown', component_property='value')
)
def line_chart(selected_year):
    filtered_mynw = mynw[mynw['Date'].dt.strftime('%Y') == selected_year]
    line_fig = px.line(filtered_mynw, x='Date', y='Balance', title=f'Annual Trend ({selected_year})')
    return line_fig

# Expenses by category
@app.callback(
    Output(component_id='expenses-by-category-graph', component_property='figure'),
    Input(component_id='year-dropdown', component_property='value')
)
def pie_chart(selected_year):
    filtered_mynw = mynw[mynw['Date'].dt.strftime('%Y') == selected_year]
    pie_fig = px.pie(filtered_mynw, values='Expenses', names='Categories', title=f'Expenses by category ({selected_year})')
    return pie_fig

if __name__ == '__main__':
    app.run_server(debug=True)
    
