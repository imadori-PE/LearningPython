import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Define the animate function with parameters
def animate(i, frequency, amplitude):
    ax.clear()  # Clear the current plot
    
    x = np.linspace(0, 2 * np.pi, 100)
    y = amplitude * np.sin(frequency * x + i * 0.1)  # Update the sine wave with parameters

    ax.plot(x, y)
    ax.set_ylim(-amplitude - 0.5, amplitude + 0.5)  # Set y-axis limits based on amplitude
    ax.set_title(f"Frame {i} - Frequency: {frequency}, Amplitude: {amplitude}")

# Create the figure and axis
fig, ax = plt.subplots()

# Define parameters
frequency = 2
amplitude = 1

# Create the animation with parameters
ani = FuncAnimation(
    fig,
    animate,
    fargs=(frequency, amplitude),  # Pass parameters to animate function
    frames=100,
    interval=50
)

# Display the animation
plt.show()

# Optionally save the animation
# ani.save('sine_wave_animation_with_params.mp4', writer='ffmpeg')
