import numpy as np
import cv2

def salt_pepper_noise(moon):
        # salt and peppering manually
    rows, cols = moon.shape
    salt_vs_pepper_ratio = 0.5
    amount = 0.007
    moon_salted_and_peppered = moon.copy()
    num_salt = np.ceil(amount * moon.size * salt_vs_pepper_ratio)
    coords = [np.random.randint(0, i - 1, int(num_salt)) for i in moon.shape]
    moon_salted_and_peppered[coords] = 255
    num_pepper = np.ceil(amount * moon.size * (1 - salt_vs_pepper_ratio))
    coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in moon.shape]
    moon_salted_and_peppered[coords] = 0
        
    return moon_salted_and_peppered
    


def gauus_nosie (img, mean, sigma):
    gauss = np.random.normal(mean,sigma,img.size)
    gauss = gauss.reshape(img.shape[0],img.shape[1]).astype('uint8')
    img_gauss = cv2.add(img,gauss)
    
    return img_gauss