import dash
from dash import html, dcc

dash.register_page(__name__, path='/', name='Inicio')

layout = html.Div(children=[
    html.Div([
        html.H2("Hola, soy Luis 👋"),
        dcc.Markdown(r"""
            Soy estudiante de Computación Científica en la Universidad Nacional Mayor de San Marcos.  
            Me apasiona el desarrollo de software, la simulación numérica y la aplicación de la programación en la resolución de problemas científicos.  
            Actualmente, estoy fortaleciendo mis conocimientos en estructuras de datos, modelamiento matemático y visualización científica.  
            Busco seguir aprendiendo y participar en proyectos donde la ciencia y la tecnología se encuentren.
        """),
    ],className="text"),

    html.Div([
        html.Img(src="assets/images/hero-headshot.webp", alt="Luis Hernández headshot")
    ],className="headshot")
],className="hero-section")