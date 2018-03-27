# #!/usr/bin/env python
# from images2gif import writeGif
# from PIL import Image
# import os

# file_names = ['cat1.jpg', 'cat2.jpg', 'cat3.jpg', 'cat4.jpg', 'cat5.png']

# images = [Image.open(fn) for fn in file_names]

# size = (600,350)
# for im in images:
#     im.thumbnail(size, Image.ANTIALIAS)

# filename = "cat.gif"
# writeGif(filename, images, duration=0.5, subRectangles=False)
#-*- coding: UTF-8 -*-    
  
import imageio  
  
def create_gif(image_list, gif_name):  
  
    frames = []  
    for image_name in image_list:  
        frames.append(imageio.imread(image_name))  
    # Save them as frames into a gif   
    imageio.mimsave(gif_name, frames, 'GIF', duration = 1)  
  
    return  
  
def main():  
    image_list = ['cat1.jpg', 'cat2.jpg', 'cat3.jpg',   
                  'cat4.jpg']  
    gif_name = 'created_gif.gif'  
    create_gif(image_list, gif_name)  
  
if __name__ == "__main__":  
    main()