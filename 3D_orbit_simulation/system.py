import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import time
from IPython.display import display, clear_output

class star:
    '''
    star class
    
    attributes:
        
        r0: Initial position from central "black hole" in AU (1.496e+11 meters)
        
        v0: Initial velocity in AU/s
        
        ### Is there a better way of doing this? ###
        
        r: list of positions stored inside of object
        
        v: list of velocities stored inside of object
    '''
    
    def __init__(self, r0, v0, i = 0):
            self.r0 = r0
        
            self.v0 = v0
        
            self.pos = None
            
            self.i = i

class system2d:
    '''
    2d simulation of astronomical bodies orbiting around a large central mass 
    
    attributes:
        
        star_list : star
            list of star objects that will be orbiting around the system
    
    methods:
        
        iterate : 
            Code I stole from PHY321, uses a method known as the Velocity - Verlet method
            to propagate the motion of the stars as they orbit around the central mass
        
        plot : 
            Plots the positions of the stars at a specified point in time
    
    '''
    
    def __init__(self, star_list, M):
        
        self.star_list = star_list
        self.M = M
    
    def iterate(self,tfinal,dt):
        '''
        Stolen from PHY321, uses the the Velocity - Verlet method
        to propagate the motion of the stars as they orbit around the central mass.
        Stores position and velocity values inside of the star objects
        
        arguments:
            
            tfinal : float
                length of time at which we want to iterate over (in years)
            
            dt : float
                amount of time between each iteration. Smaller values will result
                in a more accurate measurement, but it will also make the simulation
                take longer to run
        '''
        
        for star in self.star_list:
            #set up arrays 
            n = int(tfinal/dt)
            
            star.v = np.zeros((n,2))
            star.r = np.zeros((n,2))
            
            star.v[0] = star.v0
            star.r[0] = star.r0
            
            G = 6.67e-11
            
            for i in range(n-1):
                rabs = np.sqrt(sum(star.r[i]*star.r[i])) 
                a = -G*self.M/(rabs**3)*star.r[i]
                star.r[i+1] = star.r[i] + dt*star.v[i] + dt**2/2*a
                rabs_new = np.sqrt(sum(star.r[i+1]*star.r[i+1])) 
                a_new = -G*self.M/(rabs_new**3)*star.r[i+1]
                star.v[i+1] = star.v[i] + dt/2*(a_new+a)
                
                
    def plot(self, star_list, i, xlim, ylim):
        '''
        Plots the positions of the stars at a specified point in time
        
        arguments:
        
            star_list : star
                list of star objects
            
            i : int
                which indecy from the position arrays will be plotted
            
            ### Is there a better way to do this? ###
            
            xlim: list
                the x bounds of the plot 
            
            ylim: list
                the y bounds of the plot
        '''
        for star in star_list:
            plt.scatter(star.r[i,0],star.r[i,1])
            plt.xlim(xlim)
            plt.ylim(ylim)


class system3d:
    
       
    def __init__(self, star_list, M):
        
        self.star_list = star_list
        self.M = M
    
    def iterate(self,tfinal,dt):
        '''
        Stolen from PHY321, uses the the Velocity - Verlet method
        to propagate the motion of the stars as they orbit around the central mass.
        Stores position and velocity values inside of the star objects
        
        arguments:
            
            tfinal : float
                length of time at which we want to iterate over (in years)
            
            dt : float
                amount of time between each iteration. Smaller values will result
                in a more accurate measurement, but it will also make the simulation
                take longer to run
        '''
        
        for star in self.star_list:
            #set up arrays 
            n = int(tfinal/dt)
            
            star.v = np.zeros((n,3))
            star.r = np.zeros((n,3))
            
            star.v[0] = star.v0
            star.r[0] = star.r0
            
            G = 6.67e-11
            
            for i in range(n-1):
                rabs = np.sqrt(sum(star.r[i]*star.r[i])) 
                a = -G*self.M/(rabs**3)*star.r[i]
                star.r[i+1] = star.r[i] + dt*star.v[i] + dt**2/2*a
                rabs_new = np.sqrt(sum(star.r[i+1]*star.r[i+1])) 
                a_new = -G*self.M/(rabs_new**3)*star.r[i+1]
                star.v[i+1] = star.v[i] + dt/2*(a_new+a)
            
    def plot(self, xlim, ylim, zlim):
        '''
        Plots the positions of the stars at a specified point in time
        
        arguments:
        
            star_list : star
                list of star objects
            
            i : int
                which indecy from the position arrays will be plotted
            
            ### Is there a better way to do this? ###
            
            xlim: list
                the x bounds of the plot 
            
            ylim: list
                the y bounds of the plot
        '''
        fig = plt.figure()
        ax = plt.axes(projection='3d')

        tf = 100
        dt = 0.001

        n = np.arange(0,tf*1/dt,50)
        
        for i in n:
            for star in self.star_list:
                ax.scatter3D(star.r[int(i), 0], star.r[int(i), 1], star.r[int(i), 2])
                
            ax.set_xlim([-5,5])
            ax.set_ylim([-5,5])
            ax.set_zlim([-5,5])
            
            display(fig)

            time.sleep(0.25)

            plt.cla()

            clear_output(wait=True) 





