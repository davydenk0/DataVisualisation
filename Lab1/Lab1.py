import sys
import matplotlib.pyplot as plt
import numpy as np

def task1():
    def y_function(x):
        return (2 + x**2) / (1 + x * np.exp(-x**3) * np.sin(x)**2)

    def z_function(x):
        if x < 0:
            return (1 + 5*x**3 + x**2)
        elif 0 <= x < 1:
            return np.sin(x)**2 / (5 + x)
        else:
            return np.sin(x + 1)**2 * np.exp(0.6 * x)

    x = np.linspace(-2, 2, 100)
    y = [y_function(val) for val in x]
    z = [z_function(val) for val in x]

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label='y = (2 + x^2) / (1 + xe^(-x^3)sin^2(x))')
    plt.plot(x, z, label='z based on condition')
    plt.title('Graphs of y and z Functions')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.grid(True)
    plt.show()

def task2():
    x = np.linspace(-2, 2, 100)
    y = np.linspace(-2, 2, 100)

    X, Y = np.meshgrid(x, y)

    Z = 10 * Y * np.tan(X**3 + 1) + np.sin(X**2 + 10 * Y)

    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')

    ax.plot_surface(X, Y, Z, cmap='viridis')

    ax.set_title('3D Surface Plot: z = 10ytan(x^3+1)+sin(x^2+10y)')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')

    plt.show()

def task3():
    a = 1
    phi = np.linspace(0, 2 * np.pi, 100)

    p_squared = 2 * a**2 * np.cos(2 * phi)
    p = np.sqrt(np.abs(p_squared))

    plt.figure(figsize=(8, 6))
    plt.polar(phi, p, label='p^2 = 2a^2cos(2phi)')
    plt.title('Графік поверхні у полярних координатах')
    plt.legend()
    plt.grid(True)
    plt.show()

def task4():
    a = 2
    b = 1
    c = 1

    x = np.linspace(-a, a, 100)
    y = np.linspace(-b, b, 100)

    X, Y = np.meshgrid(x, y)

    Z = ((X ** 2 / a ** 2) + (Y ** 2 / b ** 2)) / (2 * c)

    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')

    ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.7)

    ax.set_title("Поверхня другого порядку")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_zlabel("Z-axis")

    plt.show()

def task5():
    years = [1900, 1913, 1929, 1938, 1950, 1960, 1970, 1980, 1990, 2000]
    germany = [21.5, 54, 58, 64.1, 36.5, 87.5, 185, 385, 600, 710]
    france = [22, 28.5, 40.5, 40, 31.5, 62.5, 140, 235, 330, 420]
    uk = [38.5, 54.5, 73, 76, 66, 105, 160, 235, 320, 400]
    belgium = [12.2, 15.5, 18.4, 16.8, 12.3, 27.5, 63, 112, 176, 214]

    plt.figure(figsize=(10, 8))
    plt.subplot(2, 1, 1)
    plt.bar(years, germany, width=3, label='Germany')
    plt.bar(years, france, width=3, label='France', bottom=germany)
    plt.bar(years, uk, width=3, label='Great Britain', bottom=[germany[i] + france[i] for i in range(len(germany))])
    plt.bar(years, belgium, width=3, label='Belgium', bottom=[germany[i] + france[i] + uk[i] for i in range(len(germany))])
    plt.title('2D Stacked Bar Chart')
    plt.xlabel('Years')
    plt.ylabel('Values')
    plt.legend()
    plt.grid(True)

    ax = plt.subplot(2, 1, 2, projection='3d')  # Second chart in the second row
    x_pos = np.array(years)
    y_pos = np.zeros(len(years))
    z_pos = np.zeros(len(years))
    dx = np.ones(len(years)) * 2
    dy = np.ones(len(years)) * 2

    ax.bar3d(x_pos, y_pos, z_pos, dx, dy, germany, color='b', label='Germany')
    ax.bar3d(x_pos, y_pos + 2, z_pos, dx, dy, france, color='g', label='France')
    ax.bar3d(x_pos, y_pos + 4, z_pos, dx, dy, uk, color='r', label='Great Britain')
    ax.bar3d(x_pos, y_pos + 6, z_pos, dx, dy, belgium, color='y', label='Belgium')

    ax.set_xlabel('Years')
    ax.set_ylabel('Countries')
    ax.set_zlabel('Values')
    ax.set_yticks([0, 2, 4, 6])
    ax.set_yticklabels(['Germany', 'France', 'Great Britain', 'Belgium'])
    plt.title('3D Bar Chart')

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    match int(input("task\n->")):
        case 1:
            task1()
        case 2:
            task2()
        case 3:
            task3()
        case 4:
            task4()
        case 5:
            task5()
