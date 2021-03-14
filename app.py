"""
tuberous-sclerosis

Author: JosephOregon https://github.com/josephoregon
Website: formaui.org
Project Notes: For my son, Maui.
"""
import os
from boto.s3.connection import S3Connection
import dash
# import dash_core_components as dcc
# dash-core-components==1.15.0
import dash_html_components as html
import dash_bootstrap_components as dbc

stylesheets = [dbc.themes.BOOTSTRAP]
app = dash.Dash(external_stylesheets=[dbc.themes.LUX])
server = app.server

# s3 = S3Connection(os.environ['S3_KEY'], os.environ['S3_SECRET'])
# 's3://for-maui-project/images/formaui-logo.png'

app.title = 'For Our Maui.'

maui_logo = 'assets/formaui-logo.extension'


def greetings():
    return html.H1('For Maui.')


navbar = dbc.Navbar(
    [
        html.A(
            # Use row and col to control vertical alignment of logo / brand
            dbc.Row(
                [
                    dbc.Col(html.Img(src=maui_logo, height="70px")),
                    dbc.Col(dbc.NavbarBrand("Tuberous Sclerosis Research", className="ml-2")),
                ],
                align="center",
                no_gutters=True,
            ),
            href="https://www.instagram.com/maui__strong/",
        ),
    ],
    color="#487e95",
    dark=True,
)

footer = dbc.Container(
    dbc.Row(
        dbc.Col(
            html.P(
                [
                    html.Span('by Joseph Rosas, Data Scientist', className='mr-2'),
                    html.A(html.I(className='fas fa-envelope-square mr-1'), href='mailto:<you>@<provider>.com'),
                    html.A(html.I(className='fab fa-github-square mr-1'), href='https://github.com/<you>/<repo>'),
                    html.A(html.I(className='fab fa-linkedin mr-1'), href='https://www.linkedin.com/in/<you>/'),
                    html.A(html.I(className='fab fa-twitter-square mr-1'), href='https://twitter.com/<you>'),
                ],
                className='lead'
            )
        )
    )
)

app.layout = html.Div([
    navbar,
    html.Br(),
    # greetings(),
    html.H6('Recommended Links'),
    html.A('Tuberous Sclerosis Warrior 💪🏽', href='https://www.instagram.com/maui__strong/', target='_blank'),
    footer
])


def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


if __name__ == '__main__':
    app.run_server(debug=True)
