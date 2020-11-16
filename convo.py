import numpy as np

def convolute(image, kernel):
    
    # Flip the kernel
    kernel = np.flipud(np.fliplr(kernel))
    # convolution output
    output = np.zeros_like(image)

    # Add zero padding to the input image
    image_padded = np.zeros((image.shape[0] + kernel.shape[0]-1, image.shape[1] + kernel.shape[1]-1))
    if kernel.shape[0]==3:
        image_padded[1:-1, 1:-1] = image
    elif kernel.shape[0]==5:
        image_padded[2:image_padded.shape[0]-2, 2:image_padded.shape[1]-2] = image
    
    if kernel.shape[0]==3:
        for x in range(image.shape[1]):
            for y in range(image.shape[0]):
            # element-wise multiplication of the kernel and the image
                output[y, x]=(kernel * image_padded[y: y+3, x: x+3]).sum()
    else:
        for x in range(image.shape[1]):
            for y in range(image.shape[0]):
            # element-wise multiplication of the kernel and the image
                output[y, x]=(kernel * image_padded[y: y+5, x: x+5]).sum()

    return output