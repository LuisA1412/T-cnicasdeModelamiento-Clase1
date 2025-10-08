import dash
from dash import html, dcc
import plotly.graph_objects as go
import numpy as np

################################################

P0 = 900000 # población inicial
r = 0.2311 # tasa de crecimiento
K = 1072764 # capacidad de carga
t = np.linspace(0, 50, 50) # tiempo
P = (P0* K * np.exp(r*t)) / ((K-P0) + P0 * np.exp(r*t)) # función de crecimiento exponencial

#crear un scatter plot
trace = go.Scatter(
    x = t,
    y = P,
    mode="lines+markers",
    line=dict(
        dash='solid',
        color='black',
        width=2,
    ),
    marker=dict(
        color='blue',
        symbol='circle',
        size=6,
    ),
    name='(P0* K * e^(rt)) / ((K-P0) + P0 * e^(rt))',
    hovertemplate='t: %{x:.2f}<br>P(t): %{y:.2f}<extra></extra>',

)

# crear la figura
fig = go.Figure(data=trace)

fig.update_layout(
    title=dict(
        text='<b>Crecimiento Logístico</b>',
        font=dict(
            size=20,
            color='black',
        ),
        x=0.5,
        y=0.95,
    ),
    xaxis_title='Tiempo (t)',
    yaxis_title='Población P(t)',
    margin=dict(l=40,r=40,t=50,b=40,),
    paper_bgcolor='lightblue',
    plot_bgcolor='white',
    font=dict(
        family='Output',
        size=14,
        color='black',
    ),
)

fig.update_xaxes(
    showgrid=True,
    gridwidth=1,
    gridcolor='lightpink',

    zeroline=True,
    zerolinewidth=2,
    zerolinecolor='red',

    showline=True,
    linecolor='black',
    linewidth=2,
    mirror=True,
)

fig.update_yaxes(
    showgrid=True,
    gridwidth=1,
    gridcolor='lightpink',

    zeroline=True,
    zerolinewidth=2,
    zerolinecolor='red',

    showline=True,
    linecolor='black',
    linewidth=2,
    mirror=True,
)

################################################

dash.register_page(__name__, path='/pagina2', name='Página 2')

layout = html.Div(children=[
    #contenedor izquierdo
    html.Div(children=[
        html.H2("Crecimiento logístico y Capacidad de Carga", className="title"),
        dcc.Markdown(r"""
            La capacidad de carga de un organismo en un ambiente determinado se define como la población máxima de ese organismo que el ambiente puede sostener indefinidamente.
        """, mathjax=True),

        dcc.Markdown(r"""
            Supongamos que  $K$
            representa la capacidad de carga de un organismo concreto en un ambiente determinado, y que  $r$
            es un número real que representa la tasa de crecimiento. La función  $P(t)$
            representa la población de este organismo en función del tiempo  $t$,
            y la constante  $P_0$
            representa la población inicial (población del organismo en el tiempo  $t=0$).
            Entonces la ecuación diferencial logística es
        """,mathjax=True),

        dcc.Markdown(r"""
            $$
            \dfrac{dP}{dt} = rP\left(1-\dfrac{P}{K}\right)
            $$
        """, mathjax=True),

        html.H3("Solución de la Ecuación Diferencial Logística"),

        dcc.Markdown(r"""
            Consideremos la ecuación diferencial logística sujeta a una población inicial de $P_0$
            con capacidad de carga  $K$
            y tasa de crecimiento  $r$.
            La solución del correspondiente problema de valor inicial viene dada por
        """, mathjax=True),

        dcc.Markdown(r"""
            $$
            P(t) = \dfrac{P_0 K e^{rt}}{(K-P_0) + P_0 e^{rt}}
            $$
        """, mathjax=True),

        dcc.Markdown(r"""
            Ahora que tenemos la solución del problema de valor inicial, podemos elegir valores para  $P_0$,$r$,
            y  $K$
            y estudiar la curva de solución. Por ejemplo, utilicemos los valores  $r=0,2311$, $K=1.072.764$,
            y una población inicial de  $900.000$
            ciervos.
        """, mathjax=True),


    ], className="content left"),

    #contenedor derecho
    html.Div(children=[
        html.H2("Gráfica", className="title"),   

        dcc.Graph(
            figure=fig,
            style={'height': '420px', 'width': '100%'}
        )
    ], className="content right")  
], className="page-container")