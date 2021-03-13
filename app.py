"""
tuberous-sclerosis

Author: JosephOregon https://github.com/josephoregon
Project Notes: For my son, Maui.
"""

import dash
# import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

stylesheets = [dbc.themes.BOOTSTRAP]
app = dash.Dash(__name__, external_stylesheets=stylesheets)
server = app.server


def main():
    header_title = """ For Maui. """
    return header_title


greetings = main()

app.layout = html.Div(
    greetings
)

if __name__ == '__main__':
    app.run_server(debug=True)
