import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import time
from IPython.display import display, clear_output

class star:
    '''
    star class
    
    attributes:
        
        r0: Initial position from central "black hole" in meters
            Can be stored in both 2 and 3 Dimensions depending on which system
            class (2d or 3d) will be used
        
        v0: Initial velocity in m/s
            Must have same dimensions in r0
        
        r: list of positions stored inside of object
           values defined in the iterate() method of either system class
        
        v: list of velocities stored inside of object
           values also defined in the iterate() method of either class
    '''
    
    def __init__(self, r0, v0):
            self.r0 = r0
        
            self.v0 = v0
        
            self.r = None
            
            self.v = None
            

class system2d:
    '''
    2d simulation of astronomical bodies orbiting around a large central mass 
    
    attributes:
        
        star_list : star
            list of star objects that will be orbiting around the central mass
        
        M : float
            Mass of central black hole for which all other stars orbit around
    
    methods:
        
        iterate : 
            Uses a method known as the Velocity - Verlet method to propagate 
            the motion of the stars as they orbit around the central mass
        
        plot : 
            Plots an animation of the star's motion based on the values within
            the star objects
    
    '''
    
    def __init__(self, star_list, M):  
        self.star_list = star_list
        self.M = M
    
    def iterate(self,tfinal,dt):
        '''
        Uses the the Velocity - Verlet method to propagate the motion of the stars 
        as they orbit around the central mass.
        Stores position and velocity values inside of the star objects
        
        arguments:
            
            tfinal : float
                length of time at which we want to iterate over (seconds)
            
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
                
        print("Data Instantiation Finished")
            
    def plot(self, xlim, ylim, tf, dt):
        '''
        Plots out the paths of each star oject as a 2d animation
        
        arguments:
        
            star_list : star
                list of star objects
            
            xlim: list
                the x bounds of the plot 
            
            ylim: list
                the y bounds of the plot
            
            tf : float
                length of time at which we want to iterate over (in seconds)
            
            dt : float
                amount of time between each iteration. Smaller values will result
                in a more accurate measurement, but it will also make the simulation
                take longer to run
        '''
        
        fig = plt.figure()
        ax = plt.axes()

        n = int(tf/dt)
        
        for i in range(n):
            for star in self.star_list:
                ax.scatter(star.r[int(i), 0], star.r[int(i), 1])
                
            ax.scatter(0,0,color = "black", marker = "o")
                
            ax.set_xlim(xlim)
            ax.set_ylim(ylim)
            
            display(fig)

            time.sleep(0.00025)

            plt.cla()

            clear_output(wait=True) 

    def Escape_velocity(self,starlist):
        """Find the escape velocity of star and plot it as a function of distance
        **We will assume the radius of the star is a point**
        starlist: list of star objects to find array of distance to find
       
        """
        G = 6.67e-11
        disi=np.inf
        disf=0
        for star in starlist:
            rads = np.sqrt((star.r0[0])**2+(star.r0[1])**2)
            if rads <= disi:
                disi = rads-rads*0.8
            if rads >= disf:
                disf = rads+rads*0.1
        
        self.dis=np.linspace(disi,disf,1000)
        
        self.EV = np.sqrt(2*G*self.M/self.dis)
        plt.plot(self.dis,self.EV)
        plt.title("Escape velocity as a function of distance| Mass= "+str(self.M),y=1.05)
        plt.ylabel("Escape Velocity (m/s)")
        plt.xlabel("distance to black hole (m)")
      
        
    def ScatterStars(self,star_list,label):
        """Plots the Stars of our choice on a plot.
        star_list= list of star objets
        """
        G = 6.67e-11
        for i in range(len(star_list)):
            rad = np.sqrt((star_list[i].r0[0])**2+(star_list[i].r0[1])**2)
            vel = np.sqrt((star_list[i].v0[0])**2+(star_list[i].v0[1])**2)
            plt.scatter(rad,vel,label=str(label[i]))
            plt.title("Escape velocity as a function of distance| Mass= "+str(self.M))
            plt.ylabel("Escape Velocity (m/s)")
            plt.xlabel("distance to black hole (m)")
            plt.legend()
            
        
    def Residuals(self,star_list,label):
        """Finds the diffrence between the escape velocity from the black hole and the inital velocity of the star"""
        G = 6.67e-11
        for i in range(len(star_list)):
            rad = star_list[i].r0[0]
            vel = star_list[i].v0[1]
            EVE = np.sqrt(2*G*self.M/rad)
            res = vel-EVE
            print("The residual for",label[i],"is",res)

            
class system3d:
    '''
    3d simulation of astronomical bodies orbiting around a large central mass 
    
    attributes:
        
        star_list : star
            list of star objects that will be orbiting around the central mass

        M : float
            Mass of central black hole for which all other stars orbit around

    methods:
        
        iterate : 
            Uses a method known as the Velocity - Verlet method to propagate 
            the motion of the stars as they orbit around the central mass
        
        plot : 
            Plots an animation of the star's motion based on the values within
            the star objects
        
    ''' 
    def __init__(self, star_list, M):
        self.star_list = star_list
        self.M = M
        
    def iterate(self,tfinal,dt):
        '''
        Uses the Velocity - Verlet iterative method to propagate the motion of the 
        stars as they orbit around the central mass. Stores position and velocity 
        values inside of the star objects
        
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
                
        print("Data Instantiation Finished")
            
    def plot(self, xlim, ylim, zlim, tf, dt):
        '''
        Plots out the paths of each star oject as a 3d animation
        
        arguments:
        
            star_list : star
                list of star objects
            
            xlim: list
                the x bounds of the plot 
            
            ylim: list
                the y bounds of the plot

            zlim: list
                the z bounds of the plot

            tf : float
                length of time at which we want to iterate over (in seconds)
            
            dt : float
                amount of time between each iteration. Smaller values will result
                in a more accurate measurement, but it will also make the simulation
                take longer to run
        '''
        fig = plt.figure()
        ax = plt.axes(projection='3d')

        n = int(tf/dt)
        
        for i in range(n):
            for star in self.star_list:
                ax.scatter3D(star.r[int(i), 0], star.r[int(i), 1], star.r[int(i), 2])
                
            ax.set_xlim(xlim)
            ax.set_ylim(ylim)
            ax.set_zlim(zlim)
            
            display(fig)

            time.sleep(0.00001)

            plt.cla()

            clear_output(wait=True) 
