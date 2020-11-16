import cv2
import numpy as np

def exclude_color(image, color):
    image1= image.copy()
    if color == "r":
       #replace red channel of image by zeros
       image1[:,:,2] = np.zeros([image1.shape[0], image1.shape[1]])
       
    elif  color == "g":
       #replace green channel of image by zeros
       image1[:,:,1] = np.zeros([image1.shape[0], image1.shape[1]])      
       
    elif  color == "b":
       #replace blue channel of image by zeros
       image1[:,:,0] = np.zeros([image1.shape[0], image1.shape[1]]) 
       
       
    return image1
