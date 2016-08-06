import PixelEffect
import tqdm
from PIL import Image

class Pixelator:

    def __init__(self,image,pixel_size,pixel_effect):
        self.original_image = Image.open(image,'r')
        self.pixelated_image = Image.new("RGB",self.original_image.size)
        self.pixel_size = pixel_size
        self.pixel_effect = pixel_effect
    
    def get_pixelated_image(self):
        ht,wid = self.original_image.size
        for x in tqdm.tqdm(range(0,ht,self.pixel_size)):
            for y in range(0,wid,self.pixel_size):
                
                #init rectangle boundaries
                x1,y1=x,y
                x2,y2=min(ht,x+self.pixel_size),min(wid,y+self.pixel_size)
                
                #calculate average color
                r_avg,g_avg,b_avg = 0.0,0.0,0.0
                num_pixels = (x2-x1)*(y2-y1)
                for p in range(x1,x2):
                    for q in range(y1,y2):
                        r,g,b=self.original_image.getpixel((p,q))
                        r_avg+=r
                        g_avg+=g
                        b_avg+=b
                r_avg = int(round(r_avg/num_pixels))
                g_avg = int(round(g_avg/num_pixels))
                b_avg = int(round(b_avg/num_pixels))
                r,g,b = r_avg,g_avg,b_avg

                self.pixel_effect.refresh((r,g,b))

                for p in range(0,x2-x1):
                    for q in range(0,y2-y1):
                        pixel_value = self.pixel_effect.get_pixel(p,q)
                        self.pixelated_image.putpixel((x+p,y+q),pixel_value)

        return self.pixelated_image