import numpy as np
import plotly.graph_objects as go

## Logistic Model 

def func_graficar_ecu_log(P0, r, K, t_max):
        # Generar los valores el tiempo
    t = np.linspace(0, t_max, 20)
 
    # Ecuación
    P = (P0* K * np.exp(r*t)) / ((K-P0) + P0 * np.exp(r*t))

    # Crear Gráfica de la población
    trace_poblacion = go.Scatter(
        x = t,
        y = P,
        mode='lines+markers',
        name='Población P(t)',
        line=dict(
            color='black',
            width=2,
        ),
        marker=dict(
            size=6,
            color='blue', 
            symbol='circle'
        ),

        hovertemplate='t: %{x:.2f}<br>P(t): %{y:.2f}<extra></extra>'
    )

    # Crear gráfica de la capacidad de carga
    trace_capacidad=go.Scatter(
        x = [0,t_max],
        y = [K,K],
        mode='lines',
        name='Capacidad de Carga (K)',
        line=dict(
            color='red',
            width=2,
            dash='dot'
        ),
        hovertemplate='K: %{y:.2f}<extra></extra>'
    )

    fig=go.Figure(data=[trace_poblacion,trace_capacidad])

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
        margin=dict(l=40,r=40,t=70,b=40,),
        paper_bgcolor='lightblue',
        plot_bgcolor='white',
        font=dict(
            family='Output',
            size=14,
            color='black',
        ),

        legend = dict(
            orientation ='h',
            yanchor='bottom',
            y=1.02
        )
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

        range=[-1,t_max], 
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

        range=[0,(K,K+0.1*K)]
    )

    return fig

## Gompertz Model

def func_graficar_ecu_gompertz(P0, r, K, t_max):
        # Generar los valores el tiempo
    t = np.linspace(0, t_max, 40)
 
    # Ecuación
    P = K * np.exp(-np.exp(-r * t) * (np.log(K/P0)))

    # Crear Gráfica de la población
    trace_poblacion = go.Scatter(
        x = t,
        y = P,
        mode='lines+markers',
        name='Células P(t)',
        line=dict(
            color='black',
            width=2,
        ),
        marker=dict(
            size=6,
            color='blue', 
            symbol='circle'
        ),

        hovertemplate='t: %{x:.2f}<br>P(t): %{y:.2f}<extra></extra>'
    )

    # Crear gráfica de la capacidad de carga
    trace_capacidad=go.Scatter(
        x = [0,t_max],
        y = [K,K],
        mode='lines',
        name='Capacidad de Carga (K)',
        line=dict(
            color='red',
            width=2,
            dash='dot'
        ),
        hovertemplate='K: %{y:.2f}<extra></extra>'
    )

    fig=go.Figure(data=[trace_poblacion,trace_capacidad])

    fig.update_layout(
        title=dict(
            text='<b>Crecimiento de un Tumor</b>',
            font=dict(
                size=20,
                color='black',
            ),
            x=0.5,
            y=0.95,
        ),
        xaxis_title='Tiempo en días (t)',
        yaxis_title='Número de Células P(t)',
        margin=dict(l=40,r=40,t=70,b=40,),
        paper_bgcolor='lightblue',
        plot_bgcolor='white',
        font=dict(
            family='Output',
            size=14,
            color='black',
        ),

        legend = dict(
            orientation ='h',
            yanchor='bottom',
            y=1.02
        )
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

        range=[-1,t_max], 
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

        range=[0,(K,K+0.1*K)]
    )

    return fig