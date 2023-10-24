# Import required libraries
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

import warnings

with warnings.catch_warnings():
    warnings.filterwarnings("ignore")
    
    # Code here where warnings will be suppressed

# Read the airline data into a pandas DataFrame
team_df = pd.read_csv("output.csv")
max_year = 2019
min_year = 2014

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[html.H1('Premier League Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),

                                dcc.Dropdown(id='metric-dropdown',
                                             options=[
                                                     {'label': 'Points', 'value': 'pts'},
                                                     {'label': 'Goals scored', 'value': 'scored'},
                                                     {'label': 'Goals conceded', 'value': 'conceded'},
                                                     {'label': 'Expected Goals', 'value': 'xG'},
                                                     {'label': 'Expected Points', 'value': 'xPts'}
                                                     ],
                                             value='pts',
                                             placeholder='Select a performance metric here',
                                             searchable=True
                                             ),
                                html.Br(),
                                html.Br(),

                                dcc.Dropdown(id='type-dropdown',
                                             options=[
                                                     {'label': 'Average', 'value': 'mean'},
                                                     {'label': 'Total', 'value': 'sum'}
                                                     ],
                                             value='sum',
                                             placeholder='Select Total or average metric here',
                                             searchable=True
                                             ),
                                html.Br(),
                                html.Br(),

                               
                                html.Br(),
                                html.Br(),

                                html.P("Season:"),
                                
                                dcc.Dropdown(id='season',
                                             options=[
                                                     {'label': '2014', 'value': '2014'},
                                                     {'label': '2015', 'value': '2015'},
                                                     {'label': '2016', 'value': '2016'},
                                                     {'label': '2017', 'value': '2017'},
                                                     {'label': '2018', 'value': '2018'},
                                                     {'label': '2019', 'value': '2019'}
                                                     ],
                                             value='2014',
                                             placeholder='Select a season',
                                             searchable=True
                                             ),

                                html.Div(dcc.Graph(id='chart')),
                                ])

# Add a callback function for `metric-dropdown` as input, `chart` as output
@app.callback(Output(component_id='chart', component_property='figure'),
              [Input(component_id='metric-dropdown', component_property='value'),
               Input(component_id='type-dropdown', component_property='value'),
               Input(component_id='season', component_property='value')])

def get_barplot(metric, typee, season):
    year = float(season)
    filtered_df = team_df[team_df['season'] == year]
    if typee == 'sum':
        filtered_df = filtered_df.groupby('team_name')[metric].sum().reset_index().sort_values(by=metric, ascending=False)
    else:
        filtered_df = filtered_df.groupby('team_name')[metric].mean().reset_index().sort_values(by=metric, ascending=False)

    fig = px.bar(filtered_df, x='team_name', y=metric, title=f'{metric} by Team in {year}')
    fig.update_xaxes(title='Team Name')
    fig.update_yaxes(title=metric)
    return fig

# Run the app
if __name__ == '__main__':
  app.run_server(debug=True, port=3000)  # Use an allowed port number