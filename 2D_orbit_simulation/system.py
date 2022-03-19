import numpy as np
import matplotlib.pyplot as plt

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
    
    def __init__(self, r0, v0):
        
#         self.mass = mass # might not need since black hole is so massive
        
        self.r0 = r0
        
        self.v0 = v0
        
        self.r = None
        
        self.v = None


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
    
    def __init__(self, star_list):
        
        self.star_list = star_list
    
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
            
            G = 6.674e-11/(1.495978707e11)**3
            M = 1.989e30*4e6
            for i in range(n-1):
                rabs = np.sqrt(sum(star.r[i]*star.r[i]))
                a = G*M*star.r[i]/(rabs**3)
                star.r[i+1] = star.r[i] + dt*star.v[i] + dt**2/2*a
                rabs_new = np.sqrt(sum(star.r[i+1]*star.r[i+1]))
                a_new = G*M*star.r[i+1]/(rabs_new**3)
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
    
    def __init__(self,star_list):
        
        self.star_list = star_list
    
    def iterate(self,tfinal,dt):
        
        for star in self.star_list:
            #set up arrays 
            n = int(tfinal/dt)
            star.v = np.zeros((n,3))
            star.r = np.zeros((n,3))
            
            star.v[0] = star.v0
            star.r[0] = star.r0
            
            Fourpi2 = 4*np.pi*np.pi
            for i in range(n-1):
                rabs = np.sqrt(sum(star.r[i]*star.r[i]))
                a =  -Fourpi2*star.r[i]/(rabs**3)
                star.r[i+1] = star.r[i] + dt*star.v[i] + dt**2/2*a
                a_new = -Fourpi2*star.r[i+1]/(rabs**3)
                star.v[i+1] = star.v[i] + dt/2*(a_new+a)        

    def plot(self, i, xlim, ylim,zlim):
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
        for star in self.star_list:
            fig = plt.figure()
            ax = plt.axes(projection='3d')
            ax.scatter(star.r[:,0],star.r[:,1],star.r[:,2])
            ax.set_xlim(xlim)
            ax.set_ylim(ylim)
#             ax.set_z_lim(zlim)
        
        
        
        
        