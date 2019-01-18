import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode, iplot, plot
import numpy as np
import pandas as pd

obbey = pd.read_csv('http://think.cs.vt.edu/corgis/csv/cars/cars.csv')

obbey.rename({'City mpg': 'Miles-per-gallon in city','Highway mpg': 'Miles-per-gallon in highway','Make': 'Manufacturer'},axis='columns', inplace=True)

obbey.drop(['Engine Type', 'Height', 'Length','Number of Forward Gears', 'Torque','Transmission','Hybrid','Width','Model Year', 'Classification'], axis=1)


################################################################################

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(
        children='Semester Project',
    ),
    dcc.Markdown('''
### Car statistics
The **Boxplot** compares **miles-per-gallon** consumption in city and highway between various different car manufacturers.\n
The **Histogram** illustrates amount of **horsepower** depending on **driveline**.\n
The **Pie Chart** shows most common **types of fuel** used.
    '''),
    html.Div(id='graph_container', children=[
        dcc.Dropdown(
            id='graph_types',
            options=[
                {'label': 'Cars by Fuel Type', 'value': 'cars_by_fuel_type'},
                {'label': 'Miles per gallon in city and highway', 'value': 'miles_per_gallon_city_highway'},
                {'label': 'Horsepower by driveline', 'value': 'horsepower_by_driveline'},

                ],
                value='horsepower_by_driveline'
            ),
    html.Div(id='radio_container', children=[
        dcc.RadioItems(
            options=[
            {'label': 'Miles per gallon in highway', 'value': 'miles_per_gallon_highway'},
            {'label': 'Miles per gallon in city', 'value': 'miles_per_gallon_city'},
            ],
            value='miles_per_gallon_city',
            id='radio_input'
            )
    ])
  ]),
    dcc.Graph(id='my_graph',
    ),
])

@app.callback(Output('radio_container', 'style'), [Input('graph_types', 'value')])
def toggle_container(toggle_value):
        if toggle_value == 'miles_per_gallon_city_highway':
            return {'display': 'block'}
        else:
            return {'display': 'none'}

@app.callback(
    Output(component_id='my_graph', component_property='figure'),
    [Input('graph_types', 'value'),
    Input('radio_input', 'value')]
)
def update_output_div(graph_type, box_type):
    if graph_type == 'cars_by_fuel_type':
        values = []
        for ftype in obbey["Fuel Type"].unique():
            count = obbey[(obbey["Fuel Type"] == ftype)]["Fuel Type"].count()
            values.append(count)
        fig = {
  "data": [
    {
      "values": values,
      "labels": obbey["Fuel Type"].unique(),
      "hoverinfo": "label+percent",
      "type": "pie"
    }],
    "layout": {
        "title":"Cars by Fuel Type",
            }
}

    elif graph_type == 'miles_per_gallon_city_highway':
        if box_type == 'miles_per_gallon_highway':
            data = []
            for mtype in obbey.Manufacturer.unique():
                trace = go.Box(
                x = obbey[(obbey.Manufacturer == mtype)].Manufacturer,
                y = obbey[(obbey.Manufacturer == mtype)]["Miles-per-gallon in highway"],
                name = mtype,
        )
                data.append(trace)

            layout = go.Layout(
    title = 'Miles per gallon in Highway',
    showlegend = True,
    yaxis=dict(
        title="Miles per gallon"),
    xaxis=dict(
        title=""),
)

            fig = dict(data=data, layout=layout)
        else:
            data = []
            for mtype in obbey.Manufacturer.unique():
                trace = go.Box(
                x = obbey[(obbey.Manufacturer == mtype)].Manufacturer,
                y = obbey[(obbey.Manufacturer == mtype)]["Miles-per-gallon in city"],
                name = mtype,
        )
                data.append(trace)

            layout = go.Layout(
    title = 'Miles per gallon in City',
    showlegend = True,
    yaxis=dict(
        title="Miles per gallon"),
    xaxis=dict(
        title=""),
)

            fig = dict(data=data, layout=layout)
    else:
        trace1 = go.Histogram(
    x=obbey[(obbey.Driveline == "All-wheel drive")].Horsepower,
    name = 'All-wheel drive'
)
        trace2 = go.Histogram(
    x=obbey[(obbey.Driveline == "Front-wheel drive")].Horsepower,
    name = 'Front-wheel drive'
)
        trace3 = go.Histogram(
    x=obbey[(obbey.Driveline == "Rear-wheel drive")].Horsepower,
    name = 'Rear-wheel drive'
)
        trace4 = go.Histogram(
    x=obbey[(obbey.Driveline == "Four-wheel drive")].Horsepower,
    name = 'Four-wheel drive'
)

        data = [trace1, trace2, trace3, trace4]
        layout = go.Layout(
    title = 'Horsepower by driveline'
)
        fig = go.Figure(data=data, layout=layout)

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
