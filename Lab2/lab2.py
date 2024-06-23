import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mayavi import mlab
import glyph_visualization_lib as gvl

# Define the functions for each task

def task1():
    # Task 1: Visualize the Scalar Field and its Gradient
    def u(x, y):
        return x * np.sqrt(y) - y * x**2

    def grad_u(x, y):
        du_dx = np.sqrt(y) - 2 * y * x
        du_dy = (1 / (2 * np.sqrt(y))) * x - x**2
        return du_dx, du_dy

    # Define the domain
    x = np.linspace(0, 9, 100)
    y = np.linspace(0, 9, 100)
    X, Y = np.meshgrid(x, y)
    Z = u(X, Y)

    # Plot the scalar field using a contour plot
    plt.figure(figsize=(10, 6))
    contour = plt.contourf(X, Y, Z, cmap='viridis', levels=50)
    plt.colorbar(contour)
    plt.title('Scalar Field $u(x, y) = x \sqrt{y} - y x^2$')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

    # Compute the gradient over the domain
    U, V = grad_u(X, Y)

    # Plot the gradient as a vector field using a quiver plot
    plt.figure(figsize=(10, 6))
    plt.contourf(X, Y, Z, cmap='viridis', levels=50)
    plt.colorbar()
    plt.quiver(X, Y, U, V, color='white')
    plt.title('Gradient of Scalar Field $\\nabla u(x, y)$')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

def task2():
    # Task 2: Visualize a Plane Vector Field
    def F(x, y):
        Fx = x + y
        Fy = x - y
        return Fx, Fy

    # Define the domain
    x = np.linspace(-9, 9, 20)
    y = np.linspace(-9, 9, 20)
    X, Y = np.meshgrid(x, y)
    Fx, Fy = F(X, Y)

    # Plot the vector field using quiver plot
    plt.figure(figsize=(10, 6))
    plt.quiver(X, Y, Fx, Fy, color='blue')
    plt.title('Vector Field $\\mathbf{F} = (x + y, x - y)$')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.show()

    # Plot the vector field using streamplot
    x = np.linspace(-9, 9, 100)
    y = np.linspace(-9, 9, 100)
    X, Y = np.meshgrid(x, y)
    Fx, Fy = F(X, Y)

    plt.figure(figsize=(10, 6))
    plt.streamplot(X, Y, Fx, Fy, color='blue')
    plt.title('Streamlines of Vector Field $\\mathbf{F} = (x + y, x - y)$')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.show()

def task3():
    # Task 3: Construct a Three-Dimensional Visualization of the Vector Field
    def F_3D(x, y, z):
        Fx = 1 / y
        Fy = 1 / z
        Fz = 1 / x
        return Fx, Fy, Fz

    # Define the domain
    x = np.linspace(-9, 9, 10)
    y = np.linspace(-9, 9, 10)
    z = np.linspace(-9, 9, 10)
    X, Y, Z = np.meshgrid(x, y, z)

    # Compute the vector field
    Fx, Fy, Fz = F_3D(X, Y, Z)

    # Plot the vector field using quiver3D
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.quiver(X, Y, Z, Fx, Fy, Fz, length=1.0, normalize=True, color='blue')
    ax.set_title('3D Vector Field $\\mathbf{F} = \\left( \\frac{1}{y}, \\frac{1}{z}, \\frac{1}{x} \\right)$')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()

def task4():
    # Task 4: Construct a Visualization of a Tensor Field using mayavi and glyph_visualization_lib
    x = np.linspace(0, np.pi, 8, dtype=float, endpoint=True)
    y = np.linspace(-np.pi, -1, 8, dtype=float, endpoint=True)
    z = np.linspace(0, 2 * np.pi, 8, dtype=float, endpoint=True)
    X, Y, Z = np.meshgrid(x, y, z)

    stress_tensor = np.array([
        [-np.sin(X), 5 * np.sin(X + Y), 10 * np.sin(X * Z)],
        [5 * np.sin(X + Y), -np.sin(Y), 3 * np.sin(Y + Z)],
        [10 * np.sin(X * Z), 3 * np.sin(Y + Z), np.cos(Z)]
    ])

    vm_stress = gvl.get_von_Mises_stress(stress_tensor)
    glyph_radius = 0.25
    limits = [np.min(vm_stress), np.max(vm_stress)]
    colormap = plt.get_cmap('rainbow', 120)

    fig = mlab.figure(bgcolor=(1, 1, 1))
    fig2 = plt.figure()
    ax = fig2.add_subplot(111, projection='3d')

    for i in range(x.size):
        for j in range(y.size):
            for k in range(z.size):
                center = [x[i], y[j], z[k]]
                data = stress_tensor[:, :, i, j, k]
                color = colormap(gvl.get_colormap_ratio_on_stress(vm_stress[i, j, k], limits))[:3]

                x_g, y_g, z_g = gvl.get_glyph_data(
                    center, data, limits, glyph_points=12, glyph_radius=glyph_radius,
                    glyph_type=3, superquadrics_option=2
                )

                mlab.mesh(x_g, y_g, z_g, color=color)

    mlab.move(forward=1.8)
    mlab.savefig("superquadric-Kindlmann_modified-viz.png", size=(100, 100))
    mlab.show()

# Main function to select and run tasks
if __name__ == '__main__':
    task = int(input("Select task (1-4):\n-> "))
    match task:
        case 1:
            task1()
        case 2:
            task2()
        case 3:
            task3()
        case 4:
            task4()
        case _:
            print("Invalid task number.")
