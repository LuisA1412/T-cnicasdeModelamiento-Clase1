import dash
from dash import html, dcc

dash.register_page(__name__, path='/', name='Inicio')

layout = html.Div([
    html.H1("Bienvenidos al Inicio")
])