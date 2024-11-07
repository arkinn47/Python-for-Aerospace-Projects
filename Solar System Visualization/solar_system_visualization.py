import sys                              
import numpy as np                      
import matplotlib.pyplot as plt         
from mpl_toolkits.mplot3d import Axes3D  


# Define data for planets
planet_names = [
    'Mercury',
    'Venus',
    'Earth',
    'Mars',
    'Jupiter',
    'Saturn',
    'Uranus',
    'Neptune']
semi_major_axis = [0.39, 0.72, 1.0, 1.52, 5.2, 9.58,
                   19.22, 30.05]  # in AU (astronomical units)
orbit_period = [0.24, 0.62, 1.0, 1.88, 11.86, 29.46, 84.01, 164.8]  # in years

# Define background as black
plt.style.use('dark_background')

def create_visualization(dimensions = None):
    '''Create 2d or 3d visualization.'''
    dimension = dimensions
    if dimension is not None:
        figure3d, axes3d = plt.subplots(figsize=(9, 9))
        if dimension == 'both':
            figure2d, axes2d = plt.subplots(figsize=(9, 9))
    else:
        figure3d, axes3d = plt.subplots(figsize=(9, 9))
        figure2d, axes2d = plt.subplots(figsize=(9, 9))

    if dimension == '3d':
        axes3d = figure3d.add_subplot(111, projection='3d')
        axes3d.scatter(0, 0, 0, color='yellow', s=50, label='Sun')
    elif dimension == '2d':
        axes3d.scatter(0, 0, color='yellow', s=50, label='Sun')
    elif dimension == 'both' or dimension is None:
        #Create 2d plot.
        axes3d = figure3d.add_subplot(111, projection='3d')
        axes3d.scatter(0, 0, 0, color='yellow', s=50, label='Sun')
        #Create 3d plot.
        axes2d.scatter(0, 0, color='yellow', s=50, label='Sun')


    for i, planet in enumerate(planet_names):
        orbital_angles = np.linspace(0, 2 * np.pi, 100)
        orbital_radius = semi_major_axis[i]
        x = orbital_radius * np.cos(orbital_angles)
        y = orbital_radius * np.sin(orbital_angles)

        if dimension == '3d':
            z = np.zeros_like(x)
            axes3d.plot(x, y, z, label=planet)
        elif dimension == '2d':
            axes3d.plot(x, y, label=planet)
        elif dimension == 'both' or dimension is None:
            z = np.zeros_like(x)
            axes2d.plot(x, y, label=planet)
            axes3d.plot(x, y, z, label=planet)


    if dimension == '3d':
        axes3d.set_xlabel('Distance (AU)')
        axes3d.set_ylabel('Dsitance (AU)')
        axes3d.set_zlabel('Dsitance (AU)')
        axes3d.set_title('Solar System')
        axes3d.legend()
    elif dimension == '2d':
        axes3d.set_xlabel('Distance (AU)')
        axes3d.set_ylabel('Dsitance (AU)')
        axes3d.set_title('Solar System')
        axes3d.legend()
    elif dimension == 'both' or dimension is None:
        #Set 2d plot.
        axes2d.set_xlabel('Distance (AU)')
        axes2d.set_ylabel('Dsitance (AU)')
        axes2d.set_title('Solar System')
        axes2d.legend()
        #Set 3d plot.
        axes3d.set_xlabel('Distance (AU)')
        axes3d.set_ylabel('Dsitance (AU)')
        axes3d.set_zlabel('Dsitance (AU)')
        axes3d.set_title('Solar System')
        axes3d.legend()

    plt.grid(True)
    plt.show()
