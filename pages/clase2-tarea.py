import dash
from dash import html, dcc, Input, Output, State, callback
import numpy as np
import plotly.graph_objects as go
from utils.funciones import func_graficar_ecu_gompertz

dash.register_page(__name__, path='/pagina4', name='Página 4')


## Layout de la página ##

layout = html.Div(children=[
    #contenedor izquierdo
    html.Div([
        html.H2("Parámetros del Modelo", className="title"),

        html.Div([
            html.Label("Número Inicial de Células P(0):"),
            dcc.Input(id="input-p0", type="number", value=1, className="input-field"),
        ], className="input-group"),

        html.Div([
            html.Label("Tasa de Crecimiento (r):"),
            dcc.Input(id="input-r", type="number", value=0.1, step=0.01 ,className="input-field"),
        ], className="input-group"),

        html.Div([
            html.Label("Capacidad de Carga (K): "),
            dcc.Input(id="input-k", type="number", value=10e6, step = 10e5, className="input-field"),
        ], className="input-group"),

        html.Div([
            html.Label("Tiempo Máximo (t):"),
            dcc.Input(id="input-t", type="number", value=100, className="input-field"),
        ], className="input-group"),

        html.Button("Generar Gráfica", id='btn-generar', className="btn-generar"),
    ], className="content left"),

    #contenedor derecho
    html.Div(children=[
        html.H2("Gáfica", className="title"),

        dcc.Graph(
            id = 'grafica-poblacion',
            style={'height':'350px','width':'100%'},
        )
    ], className="content right")
], className="page-container")


## Callbacks ##

@callback(
    Output('grafica-poblacion', 'figure'),
    Input('btn-generar', 'n_clicks'),
    State('input-p0', 'value'),
    State('input-r', 'value'),
    State('input-k', 'value'),
    State('input-t', 'value'),
    prevent_initial_call=False,
    allow_duplicate=True
)

def actualizar_grafica(n_clicks, P0, r, K, t_max):
    
    fig = func_graficar_ecu_gompertz(P0, r, K, t_max)
    return fig
 