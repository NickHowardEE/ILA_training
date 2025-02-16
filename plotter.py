# ~~~ IMPORTS ~~~
# Python libraies.
import math
import plotly.graph_objects as go
import numpy as np
# Custom libraries.
import beameqs

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

def plot_frequency(nf,beam):
    period = 1/nf
    frame_frequency = 0.1
    frames_per_period = period / frame_frequency
    print (frames_per_period)
    num_cycles = 10 # Number of cycles in animation.
    num_frames = int(num_cycles*frames_per_period) # Number of frames in the animation.
    num_beam_elements = 10 # Number of elements in the beam.

    # Generate x and y data structures.
    y_data = np.linspace(0, beam.L, num_beam_elements) # y_data is the distance from the fixed end of the beam.
    mode_displacements = []
    for y in y_data:
        mode_displacements.append(beameqs.mode_shape(y, beam))
    x_data = [] # x_data is time varying.
    # Calculate the time varying x data.
    for i in range(0, num_frames):
        period = num_frames / num_cycles
        multiplier = math.sin((2*math.pi/period)*i) # The deflection is based on a sinusoidial function for animation.
        x_data.append([multiplier*i for i in mode_displacements])
            
    # Create the animated plot.
    fig = go.Figure(
        data=[go.Scatter(x=x_data[0], y=y_data)],
        layout=go.Layout(
            xaxis=dict(range=[-5, 5]),
            yaxis=dict(range=[0, beam.L + beam.L/5]),
            title="Animated Natural Frequency",
            updatemenus=[
                dict(
                    type="buttons",
                    buttons=[
                        dict(
                            label="Play",
                            method="animate",
                            args=[
                                None,
                                {
                                    "frame": {"duration": 90, "redraw": True},  # Adjust frame duration
                                    "fromcurrent": True,
                                    "loop:": True,
                                    "transition": {"duration": 0, "easing": "linear"},  # Add transition
                                },
                            ],
                        )
                    ],
                )
            ],
        ),
        frames=[
            go.Frame(data=[go.Scatter(x=x_data[i], y=y_data)])
            for i in range(1, num_frames)
        ],
    )

    fig.show()
