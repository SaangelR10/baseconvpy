from dash import dcc,Dash,html
from dash.dependencies import Input, Output
import plotly.express as px

df = px.data.gapminder()
all_continents = df.continent.unique()

app = Dash(__name__)

app.layout = html.Div([
    dcc.Checklist(
        id="checklist",
        options=[{"label": x, "value": x}
                 for x in all_continents],
        value=all_continents[3:],
        labelStyle={'display': 'inline-block'}
    ),
    dcc.Graph(id="line-chart"),
])


@app.callback(
    Output("line-chart", "figure"),
    [Input("checklist", "value")])
def update_line_chart(continents):
    mask = df.continent.isin(continents)
    fig = px.line(df[mask],
                  x="year", y="lifeExp", color='country')
    return fig



app.run_server(debug=True)