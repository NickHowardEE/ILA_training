# ~~~ IMPORTS ~~~
# Python libraies.
import plotly.graph_objects as go
import numpy as np
# Custom libraries.
import ILA_training.beameqs as beameqs

def plot_deflection(P, beam, scale_factor):
    # Generate x values
    y = np.linspace(0, beam.L, 100)
    # Calculate y values using the equation
    x = [scale_factor*beameqs.deflection(i, P, beam) for i in y]
    # Create the plot
    fig = go.Figure(data=[go.Scatter(x=x, y=y)])
    # Customize the plot (optional)
    fig.update_layout(
        title="Deflection of a cantilever beam",
        xaxis_title="Scaled deflection (m)",
        yaxis_title="Elevation (m)",
        xaxis_scaleanchor="y",
        xaxis_range=[0, max(x)],  # Set x-axis limits
        yaxis_range=[0, max(y)+10]   # Set y-axis limits
    )
    fig.show()
