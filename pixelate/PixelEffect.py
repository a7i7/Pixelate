from random import gauss
from Turbulence import Turbulence
from PIL import Image
import re
class PixelEffect:
    _persist_methods = ['get_pixel','refresh']

    def __init__(self, persister):
        self._persister = persister

    def __getattr__(self, attribute):
        if attribute in self._persist_methods:
            return getattr(self._persister, attribute)


class PlainFill:
    
    def __init__(self,pixel_size):
        self.pixel_size = pixel_size

    def refresh(self,color):
        self.r,self.g,self.b = color

    def get_pixel(self,x,y):
        return (self.r,self.g,self.b)


class MushyEffect:
    
    def __init__(self,pixel_size):
        self.pixel_size = pixel_size

    def refresh(self,color):
        self.r,self.g,self.b = color
        self.MAX_DEVIATION = 15

    def get_pixel(self,x,y):
        r_dev = int(gauss(0,self.MAX_DEVIATION))
        g_dev = int(gauss(0,self.MAX_DEVIATION))
        b_dev = int(gauss(0,self.MAX_DEVIATION))
        return (self.r+r_dev,self.g+g_dev,self.b+b_dev)
 
class LumenCenterEffect:
    
    def __init__(self,pixel_size):
        self.pixel_size = pixel_size
    
    def refresh(self,color):
        self.r,self.g,self.b = color
        self.mid_x = self.pixel_size/2.0
        self.mid_y = self.pixel_size/2.0

    def get_pixel(self,x,y):
        off = int(abs(x-self.mid_x)**1.5+abs(y-self.mid_y)**1.5)
        return (self.r+off,self.g+off,self.b+off)


class LumenSideEffect:
    
    def __init__(self,pixel_size):
        self.pixel_size = pixel_size

    def refresh(self,color):
        self.r,self.g,self.b = color
        self.mid_x = self.pixel_size/2.0
        self.mid_y = self.pixel_size/2.0

    def get_pixel(self,x,y):
        off = int(abs(x)**1+abs(y)**1)
        return (self.r+off,self.g+off,self.b+off)



class Colors256Effect:

    #Taken from https://gist.github.com/MicahElliott/719710
    XTERM_256_LIST = [(0, 0, 0), (128, 0, 0), (0, 128, 0), (128, 128, 0), (0, 0, 128), (128, 0, 128), 
                (0, 128, 128), (192, 192, 192), (128, 128, 128), (255, 0, 0), (0, 255, 0), 
                (255, 255, 0), (0, 0, 255), (255, 0, 255), (0, 255, 255), (255, 255, 255), (0, 0, 0), 
                (0, 0, 95), (0, 0, 135), (0, 0, 175), (0, 0, 215), (0, 0, 255), (0, 95, 0), 
                (0, 95, 95), (0, 95, 135), (0, 95, 175), (0, 95, 215), (0, 95, 255), (0, 135, 0), 
                (0, 135, 95), (0, 135, 135), (0, 135, 175), (0, 135, 215), (0, 135, 255), (0, 175, 0), 
                (0, 175, 95), (0, 175, 135), (0, 175, 175), (0, 175, 215), (0, 175, 255), (0, 215, 0), 
                (0, 215, 95), (0, 215, 135), (0, 215, 175), (0, 215, 215), (0, 215, 255), (0, 255, 0), 
                (0, 255, 95), (0, 255, 135), (0, 255, 175), (0, 255, 215), (0, 255, 255), (95, 0, 0), 
                (95, 0, 95), (95, 0, 135), (95, 0, 175), (95, 0, 215), (95, 0, 255), (95, 95, 0), 
                (95, 95, 95), (95, 95, 135), (95, 95, 175), (95, 95, 215), (95, 95, 255), 
                (95, 135, 0), (95, 135, 95), (95, 135, 135), (95, 135, 175), (95, 135, 215), (95, 135, 255), 
                (95, 175, 0), (95, 175, 95), (95, 175, 135), (95, 175, 175), (95, 175, 215), (95, 175, 255), 
                (95, 215, 0), (95, 215, 95), (95, 215, 135), (95, 215, 175), (95, 215, 215), (95, 215, 255), 
                (95, 255, 0), (95, 255, 95), (95, 255, 135), (95, 255, 175), (95, 255, 215), (95, 255, 255), 
                (135, 0, 0), (135, 0, 95), (135, 0, 135), (135, 0, 175), (135, 0, 215), (135, 0, 255), 
                (135, 95, 0), (135, 95, 95), (135, 95, 135), (135, 95, 175), (135, 95, 215), (135, 95, 255), 
                (135, 135, 0), (135, 135, 95), (135, 135, 135), (135, 135, 175), (135, 135, 215), (135, 135, 255), 
                (135, 175, 0), (135, 175, 95), (135, 175, 135), (135, 175, 175), (135, 175, 215), (135, 175, 255), 
                (135, 215, 0), (135, 215, 95), (135, 215, 135), (135, 215, 175), (135, 215, 215), (135, 215, 255), 
                (135, 255, 0), (135, 255, 95), (135, 255, 135), (135, 255, 175), (135, 255, 215), (135, 255, 255), 
                (175, 0, 0), (175, 0, 95), (175, 0, 135), (175, 0, 175), (175, 0, 215), (175, 0, 255), (175, 95, 0), 
                (175, 95, 95), (175, 95, 135), (175, 95, 175), (175, 95, 215), (175, 95, 255), (175, 135, 0), 
                (175, 135, 95), (175, 135, 135), (175, 135, 175), (175, 135, 215), (175, 135, 255), (175, 175, 0), 
                (175, 175, 95), (175, 175, 135), (175, 175, 175), (175, 175, 215), (175, 175, 255), (175, 215, 0), 
                (175, 215, 95), (175, 215, 135), (175, 215, 175), (175, 215, 215), (175, 215, 255), (175, 255, 0), 
                (175, 255, 95), (175, 255, 135), (175, 255, 175), (175, 255, 215), (175, 255, 255), (215, 0, 0), 
                (215, 0, 95), (215, 0, 135), (215, 0, 175), (215, 0, 215), (215, 0, 255), (215, 95, 0), (215, 95, 95), 
                (215, 95, 135), (215, 95, 175), (215, 95, 215), (215, 95, 255), (215, 135, 0), (215, 135, 95), 
                (215, 135, 135), (215, 135, 175), (215, 135, 215), (215, 135, 255), (215, 175, 0), (215, 175, 95), 
                (215, 175, 135), (215, 175, 175), (215, 175, 215), (215, 175, 255), (215, 215, 0), (215, 215, 95), 
                (215, 215, 135), (215, 215, 175), (215, 215, 215), (215, 215, 255), (215, 255, 0), (215, 255, 95), 
                (215, 255, 135), (215, 255, 175), (215, 255, 215), (215, 255, 255), (255, 0, 0), (255, 0, 95), 
                (255, 0, 135), (255, 0, 175), (255, 0, 215), (255, 0, 255), (255, 95, 0), (255, 95, 95), (255, 95, 135), 
                (255, 95, 175), (255, 95, 215), (255, 95, 255), (255, 135, 0), (255, 135, 95), (255, 135, 135), 
                (255, 135, 175), (255, 135, 215), (255, 135, 255), (255, 175, 0), (255, 175, 95), (255, 175, 135), 
                (255, 175, 175), (255, 175, 215), (255, 175, 255), (255, 215, 0), (255, 215, 95), (255, 215, 135), 
                (255, 215, 175), (255, 215, 215), (255, 215, 255), (255, 255, 0), (255, 255, 95), (255, 255, 135), 
                (255, 255, 175), (255, 255, 215), (255, 255, 255), (8, 8, 8), (18, 18, 18), (28, 28, 28), (38, 38, 38), 
                (48, 48, 48), (58, 58, 58), (68, 68, 68), (78, 78, 78), (88, 88, 88), (98, 98, 98), (108, 108, 108), 
                (118, 118, 118), (128, 128, 128), (138, 138, 138), (148, 148, 148), (158, 158, 158), (168, 168, 168), 
                (178, 178, 178), (188, 188, 188), (198, 198, 198), (208, 208, 208), (218, 218, 218), (228, 228, 228), 
                (238, 238, 238)]

    def __init__(self,pixel_size):
        self.pixel_size = pixel_size
    
    def refresh(self,color):
        self.r,self.g,self.b = self.get_closest_xterm(color)

    def get_closest_xterm(self,rgb):
        r,g,b=rgb
        closest_r,closest_g,closest_b = 0,0,0
        min_dist = 10**9
        for parts in Colors256Effect.XTERM_256_LIST:
            dist = abs(parts[0]-r) + abs(parts[1]-g) + abs(parts[2]-b)
            if dist<min_dist:
                min_dist = dist
                closest_r,closest_g,closest_b = parts[0],parts[1],parts[2]
        return closest_r,closest_g,closest_b

    def get_pixel(self,x,y):
        return (self.r,self.g,self.b)


class SmokeEffect:

    def __init__(self,pixel_size):
        self.pixel_size = pixel_size
        self.smokeCreator = Turbulence(self.pixel_size)

    def refresh(self,color):
        self.r,self.g,self.b = color

    def get_pixel(self,x,y):
        off = self.smokeCreator.get_turbulence(x,y,self.pixel_size if False else 256)
        return (self.r+off,self.g+off,self.b+off)