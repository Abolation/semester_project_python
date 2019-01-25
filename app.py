import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Dash'),

    html.Div(children='''
        Titanic data
    '''),

    dcc.Graph(
        id='example-graph',
    ),
    dcc.Dropdown(
        id = 'dropdown-input',
        options=[
            {'label': 'Ticket price by passengers class', 'value': 'fare_class'},
            {'label': 'Age by passengers class', 'value': 'age_class'},
        ],
        value='fare_class'
    ),
    dcc.RadioItems(
        options=[
            {'label': 'Histogram', 'value': 'hist'},
            {'label': 'Boxplot', 'value': 'boxplot'}
        ],
        value='hist',
        id='radio-input'
    )
])

@app.callback(
    Output(component_id='example-graph', component_property='figure'),
    [Input(component_id='radio-input', component_property='value')]
)
def update_figure(plot_type):
    first_fare = titanic[titanic.pclass == 1].fare
    second_fare = titanic[titanic.pclass == 2].fare
    third_fare = titanic[titanic.pclass == 3].fare

    plot_function = go.Histogram if plot_type == 'hist' else go.Box
    trace1 = plot_function(x = first_fare, opacity = 0.75, name = 'First class')
    trace2 = plot_function(x = second_fare, opacity = 0.75, name = 'Second class')
    trace3 = plot_function(x = third_fare, opacity = 0.75, name = 'Third class')

    data = [trace1, trace2, trace3]

    figure={
        'data': data,
        'layout': {
            'title': 'Ticket price based on passenger''s class',
        },

    }
    return figure

titanic = pd.read_excel('http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic3.xls')

if __name__ == '__main__':
    app.run_server(debug=True)
