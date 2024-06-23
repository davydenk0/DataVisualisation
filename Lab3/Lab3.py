import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Ellipse parameters
a = 5.0  # semi-major axis
b = 3.0  # semi-minor axis
theta = np.linspace(0, 2 * np.pi, 100)

# Rectangle dimensions
width = 2.0
height = 1.0

# Ellipse coordinates
x_ellipse = a * np.cos(theta)
y_ellipse = b * np.sin(theta)

# Initialize figure and subplots
fig, ax = plt.subplots(figsize=(12, 6))

# Plot ellipse
ax.plot(x_ellipse, y_ellipse, 'b--', label='Elliptical Path')

# Initialize rectangle
rectangle = plt.Rectangle((0, 0), width, height, fc='r', alpha=0.5)
ax.add_patch(rectangle)

# Set plot limits
ax.set_xlim(-10, 10)
ax.set_ylim(-6, 6)
ax.set_aspect('equal')
ax.legend()


def init():
    rectangle.set_xy((0, 0))  # initial position at center
    return rectangle,


def update(frame):
    x = a * np.cos(theta[frame])
    y = b * np.sin(theta[frame])

    rectangle.set_xy((x - width / 2, y - height / 2))

    return rectangle,


# Animation
ani = FuncAnimation(fig, update, frames=len(theta), init_func=init, blit=True)
ani.save('ellipse_rectangle_animation.gif', writer='pillow', fps=30)
plt.show()
