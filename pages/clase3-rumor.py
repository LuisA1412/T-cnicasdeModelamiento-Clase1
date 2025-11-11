import dash
from dash import html, dcc, callback, Input, Output, State
import numpy as np
import plotly.graph_objs as go
from scipy.integrate import odeint

dash.register_page(__name__, path='/pagina8', name='Rumor')

layout = html.Div([
    html.Div([
        html.H2("Propagación de un Rumor", className="title"),

        html.Div([
            html.Label("Tasa de transmisión del rumor (b): "),
            dcc.Input(id='input-b', type='number', value=0.004, step=0.0001, className="input-field"),
        ], className="input-group"),

        html.Div([
            html.Label("Tasa de racionalización (k): "),
            dcc.Input(id='input-k', type='number', value=0.01, step=0.001, className="input-field"),
        ], className="input-group"),

        html.Div([
            html.Label("Susceptibles iniciales (S0): "),
            dcc.Input(id='input-S0', type='number', value=266, className="input-field"),
        ], className="input-group"),

        html.Div([
            html.Label("Infectados iniciales (I0): "),
            dcc.Input(id='input-I0', type='number', value=1, className="input-field"),
        ], className="input-group"),

        html.Div([
            html.Label("Individuos racionales iniciales (R0): "),
            dcc.Input(id='input-R0', type='number', value=8, className="input-field"),
        ], className="input-group"),

        html.Div([
            html.Label("Tiempo de simulación (días): "),
            dcc.Input(id='input-tiempo', type='number', value=15, className="input-field"),
        ], className="input-group"),

        html.Button("Simular Epidemia", id='btn-simular', className="btn-generar"),

    ],className="content left"),

    html.Div([
        html.H2("Evolución del Rumor", className="title"),
        dcc.Graph(
            id='grafica-rumor',
            style={'height':'450px','width':'100%'},
        ),
    ], className="content right"),

],className="page-container")

#Modelo SIR

def modelo_rumor(y, t, b, k, N):
    S, I, R = y

    dS_dt = -b * S * I 
    dI_dt = b * S * I - k * I * R    
    dR_dt = k * I * R     

    return [dS_dt, dI_dt, dR_dt]

#Callback para actualizar la gráfica

@callback(
    Output('grafica-rumor', 'figure'),
    Input('btn-simular', 'n_clicks'),
    State('input-b', 'value'),
    State('input-k', 'value'),
    State('input-S0', 'value'),
    State('input-I0', 'value'),
    State('input-R0', 'value'),
    State('input-tiempo', 'value'),
    prevent_initial_call=False
)
def simular_sir(n_clicks, b, k, S0, I0, R0, tiempo_max):
    N = S0 + R0 + I0
    y0 = [S0, I0, R0]

    t = np.linspace(0, tiempo_max, 200)

    try: 
        solucion = odeint(modelo_rumor, y0, t, args=(b, k, N))
        S, I, R = solucion.T
    except Exception as e:
        S = np.full_like(t, S0)
        I = np.full_like(t, I0)
        R = np.full_like(t, R0)

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=t, y=S, 
        mode='lines', 
        name='Susceptibles (S)', 
        line=dict(color='blue', width=2),
        hovertemplate='Día %{x:.0f}<br>Susceptibles: %{y:.0f}<extra></extra>'
        )
    )
    
    fig.add_trace(go.Scatter(
        x=t, y=I,
        mode='lines',
        name='Infectados (I)',  
        line=dict(color='red', width=2),
        hovertemplate='Día %{x:.0f}<br>Infectados: %{y:.0f}<extra></extra>'
        )
    )
    
    fig.add_trace(go.Scatter(
        x=t, y=R,
        mode='lines',
        name='Racionalizados (R)',
        line=dict(color='green', width=2),
        hovertemplate='Día %{x:.0f}<br>Racionalizados: %{y:.0f}<extra></extra>'
        )
    )  
    
    fig.update_layout(
        title=dict(
            text = "<b>Evolución del Rumor</b>",
            x = 0.5, 
            font=dict(size=16, color='darkblue') 
        ),
        xaxis_title="tiempo (días)",
        yaxis_title="Número de personas",
        paper_bgcolor='lightcyan',
        plot_bgcolor='white',
        font=dict(family='Outfit',size=12),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.0,
            xanchor="right",
            x=0.6
        ),
        margin=dict(l=40, r=40, t=60, b=40),
    )  

    fig.update_xaxes(
        showgrid=True, gridwidth=1, gridcolor='lightpink', 
        zeroline=True, zerolinewidth= 2,zerolinecolor='black',
    )

    fig.update_yaxes(
        showgrid=True, gridwidth=1, gridcolor='lightpink', 
        zeroline=True, zerolinewidth= 2,zerolinecolor='black',
    )

    return fig