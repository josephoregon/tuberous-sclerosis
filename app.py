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

stylesheets = [dbc.themes.BOOTSTRAP]
app = dash.Dash(__name__, external_stylesheets=stylesheets)
server = app.server


def greetings():
    return html.H1('For Maui.')


app.layout = html.Div([
    greetings(),
    html.H3('Recommended Links'),
    html.A('Tuberous Sclerosis Warrior 💪🏽', href='https://www.instagram.com/maui__strong/', target='_blank'),
    html.Br(),
    html.A('Ketogenic Diet and Hypothalamic Hamartomas', href='https://www.whitneyerd.com/2020/07/vegan-plant-based'
                                                              '-ketogenic-diet.html', target='_blank')
])

if __name__ == '__main__':
    app.run_server(debug=True)
