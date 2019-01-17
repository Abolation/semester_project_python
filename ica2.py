import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode, iplot, plot
import numpy as np
import pandas as pd

obbey = pd.read_csv('./cars.csv')

obbey.rename({'City mpg': 'Miles-per-gallon in city','Highway mpg': 'Miles-per-gallon in highway','Make': 'Manufacturer'},axis='columns', inplace=True)

obbey.drop(['Engine Type', 'Height', 'Driveline', 'Horsepower', 'Length','Number of Forward Gears', 'Torque','Transmission','Hybrid','Classification','Width','Model Year', 'Classification'], axis=1)


################################################################################

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(
        children='Semester Project',
    ),
    dcc.Markdown('''
### Car fuel consumption statistics
The graphs shown below compare miles-per-gallon consumption between various different car manufacturers.
    '''),
    html.Div(id='graph_container', children=[
        dcc.Dropdown(
            id='graph_type',
            options=[
                {'label': 'Miles-per-gallon consumption by Volvo', 'value': 'mpg_consumption'},
                {'label': 'Miles-per-gallon consumption by Chevrolet', 'value': 'mpg_consumption'},
                {'label': 'Miles-per-gallon consumption by Maserati', 'value': 'mpg_consumption'},
                {'label': 'Miles-per-gallon consumption by Dodge', 'value': 'mpg_consumption'},
                {'label': 'Miles-per-gallon consumption by Ferrari', 'value': 'mpg_consumption'},
                {'label': 'Miles-per-gallon consumption by Ford', 'value': 'mpg_consumption'},
                {'label': 'Miles-per-gallon consumption by Cadillac', 'value': 'mpg_consumption'},
                {'label': 'Miles-per-gallon consumption by Rolls-Royce', 'value': 'mpg_consumption'},
                {'label': 'Miles-per-gallon consumption by AMG', 'value': 'mpg_consumption'},
                {'label': 'Miles-per-gallon consumption by Acura', 'value': 'mpg_consumption'},
                {'label': 'Miles-per-gallon consumption by Aston Martin', 'value': 'mpg_consumption'},
                {'label': 'Miles-per-gallon consumption by Honda', 'value': 'mpg_consumption'},
                {'label': 'Miles-per-gallon consumption by Hyundai', 'value': 'mpg_consumption'},
                {'label': 'Miles-per-gallon consumption by Infiniti', 'value': 'mpg_consumption'},
                {'label': 'Miles-per-gallon consumption by Jaguar', 'value': 'mpg_consumption'},
                {'label': 'Miles-per-gallon consumption by Jeep', 'value': 'mpg_consumption'},
                {'label': 'Miles-per-gallon consumption by Kia', 'value': 'mpg_consumption'},
                {'label': 'Miles-per-gallon consumption by Lamborghini', 'value': 'mpg_consumption'},
                {'label': 'Miles-per-gallon consumption by Grand Cherokee', 'value': 'mpg_consumption'},
                {'label': 'Miles-per-gallon consumption by GMC', 'value': 'mpg_consumption'},
                {'label': 'Miles-per-gallon consumption by Chrysler Group LLC', 'value': 'mpg_consumption'},
                {'label': 'Miles-per-gallon consumption by Chrysler', 'value': 'mpg_consumption'},
                {'label': 'Miles-per-gallon consumption by Buick', 'value': 'mpg_consumption'},
                {'label': 'Miles-per-gallon consumption by Bentley', 'value': 'mpg_consumption'},
                {'label': 'Miles-per-gallon consumption by BMW', 'value': 'mpg_consumption'},
                {'label': 'Miles-per-gallon consumption by Audi', 'value': 'mpg_consumption'},
                {'label': 'Miles-per-gallon consumption by Land Rover', 'value': 'mpg_consumption'},
                {'label': 'Miles-per-gallon consumption by Mazda', 'value': 'mpg_consumption'},
                {'label': 'Miles-per-gallon consumption by Maybach', 'value': 'mpg_consumption'},
                {'label': 'Miles-per-gallon consumption by Mercedes', 'value': 'mpg_consumption'},
                {'label': 'Miles-per-gallon consumption by Lotus', 'value': 'mpg_consumption'},
                {'label': 'Miles-per-gallon consumption by MINI', 'value': 'mpg_consumption'},
                {'label': 'Miles-per-gallon consumption by Lexus', 'value': 'mpg_consumption'},
                {'label': 'Miles-per-gallon consumption by Lincoln', 'value': 'mpg_consumption'},
                {'label': 'Miles-per-gallon consumption by Mercedes-Benz', 'value': 'mpg_consumption'},
                {'label': 'Miles-per-gallon consumption by Mercedes-AMG', 'value': 'mpg_consumption'},
                {'label': 'Miles-per-gallon consumption by Mitsubishi', 'value': 'mpg_consumption'},
                {'label': 'Miles-per-gallon consumption by Volkswagen', 'value': 'mpg_consumption'},
                {'label': 'Miles-per-gallon consumption by Suzuki', 'value': 'mpg_consumption'},
                {'label': 'Miles-per-gallon consumption by Subaru', 'value': 'mpg_consumption'},
                {'label': 'Miles-per-gallon consumption by Porsche', 'value': 'mpg_consumption'},
                {'label': 'Miles-per-gallon consumption by Saab', 'value': 'mpg_consumption'},
                {'label': 'Miles-per-gallon consumption by Nissan', 'value': 'mpg_consumption'},
                {'label': 'Miles-per-gallon consumption by Toyota', 'value': 'mpg_consumption'},
                {'label': 'Miles-per-gallon consumption by Scion', 'value': 'mpg_consumption'},
                {'label': 'Miles-per-gallon consumption by Mercury', 'value': 'mpg_consumption'},

            ],
         ),
]
if __name__ == '__main__':
    app.run_server(debug=True)
