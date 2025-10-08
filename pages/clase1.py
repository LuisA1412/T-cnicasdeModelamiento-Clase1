import dash
from dash import html, dcc
import plotly.graph_objects as go
import numpy as np

################################################

P0 = 100 # población inicial
r = 0.03 # tasa de crecimiento
t = np.linspace(0, 100, 10) # tiempo
P = P0 * np.exp(r*t) # función de crecimiento exponencial

#crear un scatter plot
trace = go.Scatter(
    x = t,
    y = P,
    mode="lines+markers",
    line=dict(
        dash='dot',
        color='black',
        width=2,
    ),
    marker=dict(
        color='blue',
        symbol='square',
        size=8,
    ),
    name='P(t) = P0 * e^(rt)',
    hovertemplate='t: %{x:.2f}<br>P(t): %{y:.2f}<extra></extra>',

)

# crear la figura
fig = go.Figure(data=trace)

fig.update_layout(
    title=dict(
        text='<b>Crecimiento Poblacional</b>',
        font=dict(
            size=20,
            color='black',
        ),
        x=0.5,
        y=0.92,
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

dash.register_page(__name__, path='/pagina1', name='Página 1')

layout = html.Div(children=[
    #contenedor izquierdo
    html.Div(children=[
        html.H2("Crecimiento de la Población", className="title"),
        dcc.Markdown(r"""
            Para modelar el crecimiento de la población mediante una ecuación diferencial, primero tenemos que introducir algunas variables y términos relevantes. La variable  $t$.
            representará el tiempo. Las unidades de tiempo pueden ser horas, días, semanas, meses o incluso años. Cualquier problema dado debe especificar las unidades utilizadas en ese problema en particular. La variable  $P$
            representará a la población. Como la población varía con el tiempo, se entiende que es una función del tiempo. Por lo tanto, utilizamos la notación  $P(t)$
            para la población en función del tiempo. Si  $P(t)$
            es una función diferenciable, entonces la primera derivada  $\dfrac{dP}{dt}$
            representa la tasa instantánea de cambio de la población en función del tiempo.
        """, mathjax=True),

        dcc.Markdown(r"""
            En Crecimiento y decaimiento exponencial, estudiamos el crecimiento y decaimiento exponencial de poblaciones y sustancias radiactivas. Un ejemplo de función de crecimiento exponencial es  $P(t)=P_0 e^{rt}$.
            En esta función,  $P(t)$
            representa la población en el momento  $t$, $P_0$
            representa la población inicial (población en el tiempo  $t=0$),
            y la constante  $r>0$
            se denomina tasa de crecimiento. La Figura 4.18 muestra un gráfico de  $P(t)=100e^{0,03t}$.
            Aquí  $P_0=100$
            y  $r=0,03$.
        """,mathjax=True)

    ], className="content left"),

    #contenedor derecho
    html.Div(children=[
        html.H2("Gráfica", className="title"),   

        dcc.Graph(
            figure=fig,
            style={'height': '350px', 'width': '100%'}
        )
    ], className="content right")  
], className="page-container")