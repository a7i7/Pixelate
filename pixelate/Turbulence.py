import random
class Turbulence:
   """Thanks to the following resource
      http://lodev.org/cgtutor/randomnoise.html"""

   def __init__(self,pixel_size):
      self.pixel_size = pixel_size
      self.noise = self.generate_noise()

   def generate_noise(self):
      noise = [[0.0 for i in range(self.pixel_size)] for j in range(self.pixel_size)]
      for y in range(self.pixel_size):
         for x in range(self.pixel_size):
            noise[y][x] = random.random()
            while noise[y][x]>0.5:
               noise[y][x] = random.random()
      return noise

   def smooth_noise(self,x,y):
      noiseWidth = self.pixel_size
      noiseHeight = self.pixel_size
      
      #get fractional part of x and y
      fractX = x - int(x);
      fractY = y - int(y);
      
      #wrap around
      x1 = (int(x) + noiseWidth)  % noiseWidth
      y1 = (int(y) + noiseHeight) % noiseHeight

      #neighbor values
      x2 = (x1 + noiseWidth  - 1) % noiseWidth
      y2 = (y1 + noiseHeight - 1) % noiseHeight

      #smooth the noise with bilinear interpolation
      value = 0.0
      value += fractX*fractY *self.noise[y1][x1]
      value += (1.0 - fractX)*fractY*self.noise[y1][x2]
      value += fractX*(1.0-fractY)*self.noise[y2][x1]
      value += (1.0-fractX)*(1.0-fractY)*self.noise[y2][x2]
      return value

   def get_turbulence(self,x,y,size):
      value = 0.0
      initialSize = size;
      while size>=1:
         value += self.smooth_noise(x/size, y/size) * size;
         size /= 2.0;
      return int(128.0 * value / initialSize);

