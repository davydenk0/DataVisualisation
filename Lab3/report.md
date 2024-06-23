## Davydenko Pavlo IKM-M223b
# Ellipse and Rectangle Animation

This repository contains a Python script that generates an animated GIF illustrating the movement of a rectangle along an elliptical path.

## Overview

The script uses `matplotlib` to create an animation where:
- An elliptical path is plotted.
- A rectangle moves along this path, simulating an orbit.

## Code

The Python script (`ellipse_rectangle_animation.py`) performs the following tasks:
- Defines parameters for the ellipse (semi-major axis `a` and semi-minor axis `b`).
- Sets up a rectangle with specified dimensions (width `width` and height `height`).
- Initializes a figure and plots the ellipse and rectangle.
- Defines functions for initialization (`init()`) and updating (`update(frame)`) the position of the rectangle.
- Creates an animation using `FuncAnimation` from `matplotlib.animation`.
- Saves the animation as a GIF file (`ellipse_rectangle_animation.gif`).


## Detailed Explanation

## Import Libraries:

- **matplotlib.pyplot**: Used for plotting and visualization.
- **numpy**: Essential for numerical computations, used here to generate points on the ellipse.
- **FuncAnimation** from **matplotlib.animation**: Facilitates creating animations.

## Ellipse Parameters:

- **a and b**: Semi-major and semi-minor axes of the ellipse.
- **theta**: Array of angles from 0 to \( 2\pi \) radians (360 degrees) used to generate points on the ellipse.

## Rectangle Dimensions:

- **width and height**: Dimensions of the rectangle that will move along the ellipse.

## Ellipse Coordinates:

- **x_ellipse and y_ellipse**: Arrays containing x and y coordinates of points on the ellipse based on theta.

## Initialize Figure and Axes:

- Initializes the figure and axes for plotting the animation.

## Plot Ellipse:

```python
ax.plot(x_ellipse, y_ellipse, 'b--', label='Elliptical Path')
```

- This command plots the elliptical path using `x_ellipse` and `y_ellipse` arrays.
- `'b--'` specifies a blue dashed line for the path.
- `label='Elliptical Path'` assigns a label to the plot for the legend.

## Initialize Rectangle:

```python
rectangle = plt.Rectangle((0, 0), width, height, fc='r', alpha=0.5)
ax.add_patch(rectangle)
```

- Creates a rectangle with an initial position at (0, 0), width `width`, and height `height`.
- `fc='r'` sets the rectangle color to red ('r') and `alpha=0.5` makes it semi-transparent.

## Set Plot Limits and Aspect Ratio:

```python
ax.set_xlim(-10, 10)
ax.set_ylim(-6, 6)
ax.set_aspect('equal')
ax.legend()
```

- `set_xlim` and `set_ylim` define the limits of the x and y axes, respectively.
- `set_aspect('equal')` ensures the plot maintains an equal aspect ratio.
- `ax.legend()` displays the legend for the elliptical path on the plot.

## Initialization Function (`init()`):

```python
def init():
    rectangle.set_xy((0, 0))  # initial position at center
    return rectangle,
```

- Initializes the animation by setting the rectangle's initial position at the center of the ellipse.
- Returns `rectangle,` as a tuple to indicate the objects that need to be updated.

## Update Function (`update(frame)`) for Animation:

```python
def update(frame):
    x = a * np.cos(theta[frame])
    y = b * np.sin(theta[frame])

    rectangle.set_xy((x - width / 2, y - height / 2))

    return rectangle,
```

- Updates the position of the rectangle for each frame of the animation.
- Computes `x` and `y` coordinates on the ellipse for the given frame.
- `rectangle.set_xy((x - width / 2, y - height / 2))` updates the rectangle's position based on `x` and `y`.

## Animation Creation (`FuncAnimation`):

```python
ani = FuncAnimation(fig, update, frames=len(theta), init_func=init, blit=True)
```

- Creates the animation:
  - `fig`: Figure to animate.
  - `update`: Function to call for updating each frame.
  - `frames=len(theta)`: Number of frames, equivalent to the length of `theta`.
  - `init_func=init`: Function to initialize the animation.
  - `blit=True`: Improves rendering speed by only redrawing parts that have changed.

## Save and Display Animation:

```python
ani.save('ellipse_rectangle_animation.gif', writer='pillow', fps=30)
plt.show()
```

- `ani.save('ellipse_rectangle_animation.gif', writer='pillow', fps=30)`: Saves the animation as a GIF named `'ellipse_rectangle_animation.gif'` using the Pillow