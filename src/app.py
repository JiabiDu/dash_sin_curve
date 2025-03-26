import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import numpy as np
import plotly.graph_objs as go

app = dash.Dash(__name__) #__name__ will be set to "__main__" if the script is excuted. 
server = app.server

app.layout = html.Div([   #Div mean a division/section in html
    html.H1("Sine Wave Dashboard"),
    html.Label("Enter wave period (s):  ", style={'fontSize': '30px'}),
    dcc.Input(id='period-input', type='number', value=5, step=1, style={'fontSize': '40px','width':'100px'}),
    dcc.Graph(id='sine-wave-plot')
])

@app.callback(               #this callback function will need two arguments, one for output, one for inputs.
    Output('sine-wave-plot', 'figure'),    #the sine-wave-plot is the id for the graph, figure is the data type
    [Input('period-input', 'value')]       #the period-input is the id for the input box, value is the data type
)

# dash will put the value in "period-input" and pass it to following updating function. 
# There must be a update function following the @app.callback

def update_sine_wave(period):  #you can use any function name
    x = np.linspace(0, 30, 1000)
    y = np.sin(x * (2*np.pi / period)) # y will be recalculated with given period (from the input box)

    fig = go.Figure()  #go is a plotly.graph_ojbs; i.e., it is an interactive object
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', line = dict(color = 'black', width = 4), name='Sine Wave'))  #dict(color = 'green', width = 4) is a dictionary; same as {'color': 'green', 'width': 4}
    fig.update_layout(
        title='Sine Wave with Period of {}s'.format(period),
        xaxis_title='Time',
        yaxis_title='Amplitude'
    )
    fig.update_xaxes(range=[0, 30])  # Set x-axis limits
    return fig

if __name__ == '__main__':
    app.run(debug=True,port=8051)


#after running the script, open your internet browser, and go to: http://127.0.0.1:8051

# if you change any part of the code, you need to rerun the entire script