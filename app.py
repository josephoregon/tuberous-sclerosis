"""
tuberous-sclerosis

Author: JosephOregon https://github.com/josephoregon
Website: formaui.org
Project Notes: For my son, Maui.
"""
import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc

stylesheets = [dbc.themes.BOOTSTRAP]
app = dash.Dash(external_stylesheets=[dbc.themes.LUX])
server = app.server
favicon = '<link rel="icon" type="image/x-icon" href="{}">'.format('https://for-maui-project.s3.amazonaws.com/images'
                                                                   '/favicon.ico')

app.title = 'For Maui.'

maui_logo = 'https://for-maui-project.s3.amazonaws.com/images/formaui-logo.png'

navbar = dbc.Navbar(
    [
        html.A(
            # Use row and col to control vertical alignment of logo / brand
            dbc.Row(
                [
                    dbc.Col(html.Img(src=maui_logo, height="70px")),
                    dbc.Col(dbc.NavbarBrand("Tuberous Sclerosis Research", className="ml-2"))
                ],
                align="center",
                no_gutters=True,
            ),
            href="https://www.instagram.com/maui__strong/",
        ),
        dbc.Row(
                html.H6(
                    'by Joseph Rosas, Data Scientist', id='nav-bar'
                )
        )
    ],
    color="#487e95",
    dark=True,
)

intro_paragraph = html.Div([
    html.H3('Introduction'),
    html.Div([
        dcc.Markdown('''
        **SUMMARY:** Self-dedicated research for my son, Maui and all those affected by tuberous-sclerosis (TSC).
        
        As my incredible wife continues promoting TSC awareness by using her writing skills, 
        she inspires me to dedicate a part of my life towards the same purpose.
        
        '''),
        html.Br(),
        html.Br(),
        html.H6('Recommended Links'),
        html.A('Tuberous Sclerosis Warrior 💪🏽', href='https://www.instagram.com/maui__strong/', target='_blank'),
    ])
], id='intro-paragraph')

footer = dbc.Container(
    dbc.Row(
        dbc.Col(
            html.P(
                [
                    html.Span('100% Open-Source Research. Code Available On Github, The Rosas Family', id='footer')
                ]
            )
        )
    )
)

app.layout = html.Div([
    navbar,
    html.Br(),
    intro_paragraph,
    footer
], style={'marginBottom': 100, 'marginTop': 60})


def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


if __name__ == '__main__':
    app.run_server(debug=True)
