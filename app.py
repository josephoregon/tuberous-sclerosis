"""
tuberous-sclerosis

Author: JosephOregon https://github.com/josephoregon
Website: formaui.org
Project Notes: For my son, Maui.
"""

import dash
# import dash_core_components as dcc
# dash-core-components==1.15.0
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

stylesheets = [dbc.themes.BOOTSTRAP]
app = dash.Dash(external_stylesheets=[dbc.themes.LUX])
server = app.server

app.title = 'For Our Maui.'

MAUI_LOGO = "assets/formaui-logo.png"


def greetings():
    return html.H1('For Maui.')


search_bar = dbc.Row(
    [
        dbc.Col(dbc.Input(type="search", placeholder="Search")),
        dbc.Col(
            dbc.Button("Search", color="primary", className="ml-2"),
            width="auto",
        ),
    ],
    no_gutters=True,
    className="ml-auto flex-nowrap mt-3 mt-md-0",
    align="center",
)

navbar = dbc.Navbar(
    [
        html.A(
            # Use row and col to control vertical alignment of logo / brand
            dbc.Row(
                [
                    dbc.Col(html.Img(src=MAUI_LOGO, height="50px")),
                    dbc.Col(dbc.NavbarBrand("Tuberous Sclerosis Research", className="ml-2")),
                ],
                align="center",
                no_gutters=True,
            ),
            href="https://www.instagram.com/maui__strong/",
        ),
        dbc.NavbarToggler(id="navbar-toggler"),
        dbc.Collapse(search_bar, id="navbar-collapse", navbar=True),
    ],
    color="dark",
    dark=True,
)

app.layout = html.Div([
    navbar,
    html.Br(),
    # greetings(),
    html.H6('Recommended Links'),
    html.A('Tuberous Sclerosis Warrior 💪🏽', href='https://www.instagram.com/maui__strong/', target='_blank'),
    html.Br()  # ,
    # html.A('Ketogenic Diet and Hypothalamic Hamartomas', href='https://www.whitneyerd.com/2020/07/vegan-plant-based'
    #                                                         '-ketogenic-diet.html', target='_blank')
])


# add callback for toggling the collapse on small screens
@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


if __name__ == '__main__':
    app.run_server(debug=True)
