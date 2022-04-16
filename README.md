# Simulating Steller Orbits Around Sagittarius A

Arian Andalib, Nate Gu, Elias Taira

## Introduction

While Sagittarius A (Sag A for short) has been observed many times and have been confirmed to be the center of our galaxy since as early as the 1980's, it wasn't until the 2000s that this "star" was confirmed to be a black hole. Even more recently, we have been able to observe the orbits of stars very close to the black hole. Then, using Kepler's Laws to map out the orbital path of the stars, obtain an accurate reading of what the mass of this black hole is.

![](./images/Galactic_centre_orbits.svg.png)

After a careful analysis of the astronomical data, it was found that the bleck hole weighs around $3.6^{+0.2}_{-0.4}*10^6 M_\odot$ 

The actual data for these orbits can be found below from the Wikepidia page on Sag A:

![](./images/startable.jpg)

In this experiment, we seek to understand nderlying physics behind this orbital motion. Thus we decided to try to reconstruct this system with these same orbital patterns using nothing but the gravitational forces between the orbiting stars and central black hole, as well as the initial positions and velocities of the stars as well.

To do this, we will employ the use of the **Velocity Verlet method**, an iterative method designed to solve various kinds of differential equations. In the scope of this project we will use it to solve for the positions and velocities of the nearby stars orbiting Sag A given their initial position, velocity and the gravitational force exerted on them by the central black hole all as a function of time.

The differential equation we will be solving is denoted by: $$a(r) = \frac{GM_sr}{\textbf{r}^3} $$ where $a(r)$ represents the acceleration of the star (derived from the gravitational force), $G$ represents the gravitational constant ($6.67*10^{-11} m^3 kg^{-1} s^{-2}$), $M_s$ represents the mass of Sag A, **r** represents the distance to Sag A in meters and, r represents the position vector of the star.

To obtain these initial conditions, we decided to use the **q (AU)** column for position and the  **v(%c)** column for velocity. **q (AU)** represents the distance of the star from the black hole at its **perhilion**, the closest point to the black hole in the star's orbital path. This distance is measured in **AU** or **Astronomical Units**, which represent the distance from Earth to the Sun (i.e., the distance from Earth to the Sun is 1 AU or ~1.5e11 m). However, for this project we will be working in SI units, so this will be converted into meters. **v(%c)** represents the speed of the star at this perhilion location. This is units of **%c** where 'c' represents the speed of light at $3*10^8$ m/s. We will also be using this in SI units as well (m/s).

## How the Model Works

### 2D Model

In the process of making an accurate model for the Sag A system, we decided that it would be best to first start out with a simpler model of our system in a lower dimension to ensure that the basics of our model are functioning as they should before we add any more complexity to our model. Therefore, we will first try to build our model in 2 dimensions.

The majority of our code will be found in the form of classes and objects located within the file 'system.py'. There we create objects for each star in the system ('star' class), as well as an object for simulating each star object as they move through their respecive orbits ('system2d' class).

To validate that our Velocity Verlet method is functioning as it should, we first made a simple simulation of a black hole and star system with similar masses to that of our own Sun and Earth respectively.

To do this, we must first import the libraries we will be using: Numpy and Matplotlib. While we will import more libraries in order to run some animations and make 3-D plots, those libraries will be imported in 'system.py'. Only having numpy in the notebook will be sufficient enough to initialize our data. Additionally we will also import our classes from 'system.py'

```
import numpy as np
import matplotlib.pyplot as plt

%reload_ext autoreload
%autoreload 2
from system import star, system2d
```

Now we are able to run our basic simulation.

To begin, we must first by initializing our objects for the model, starting with the 'star' objects. The only arguments required for these objects are the initial position and velocity of the star, in meters and meters/second respectively
```
r0 = [1.5e11,0] # in units of meters(m), represents the initial position in [x,y]
v0 = [0,2.98e4] # in units of meters per second (m/s), represents the initial velocity in [v_x,v_y]

test_star = star(r0,v0) # creates a star object with an initial velocity and position
```

Next we initialize our system. The arguments for this object are slightly more complex. Here we require several different arguments: The mass of the central black hole (in kg) and a list of star objects
```
black_hole_mass = 2e30 # in kilograms (kg)

test_list = [test_star] # system2d class takes in a list of star objects as an argument 
                        # can be any non-zero length in size 
                        # must only compose of star objects

test_system = system2d(test_list,black_hole_mass) # creates a 2d system object using the 
                                                  # star list and the mass of the central black hole

```

```
tf = 365*24*3600 # iterating for 1 year in units of seconds (s)
dt =  tf/1000 # Amount of time between iterations, set such that there ar 1000 iterations
test_system.iterate(tf,dt) # running the iterate method, positions and velocities are sotred within each star object
```

This 

```
plt.figure(figsize = (8,8))
plt.plot(test_star.r[:,0],test_star.r[:,1], label = "Star Orbit")
plt.scatter(0,0, color = "black", marker = "o", label = "Black Hole")
plt.xlabel("X Position (m)")
plt.ylabel("Y Position (m)")
plt.title("Simple Stellar Orbit in 2D")
plt.legend()
```

This should output a plot that is something like:

<img src="https://github.com/tairaeli/cmse202_honors_project/blob/master/images/exposplot.jpg" width="400" height="400">

As a built-in method in our system2d class, we have a function for displaying an animation of our star objects as they orbit the black hole called '.plot()' which takes in a single value for the x-bounds and another value for the y-bounds. Like the '.iterate()' function, it also takes in a final time and timestep size argument to determine how long we want the animation to run for and how smooth we want the animation to be. These values can be determined independently of the '.iterate()', but they must still be in units of seconds.

To create an animation of the prior example:
```
xlim = 1.6e11
ylim = 1.6e11

test_system.plot(xlim, ylim, tf, dt)
```
We would show the animation here. However, due to the limitations of markdown, we are unable to do so. To view this animation, with all the previous code blocks, one can go to the 2D_orbit_simulation directory to view both this example code, as well as the code we wrote using this software to simulate the orbits for Sag A.

