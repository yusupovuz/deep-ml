import numpy as np

def rgb_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminosity method.
    
    Args:
        image: RGB image as list or numpy array of shape (H, W, 3)
               with values in range [0, 255]
    
    Returns:
        Grayscale image as 2D list with integer values,
        or -1 if input is invalid
    """
    # Write your code here
    arr = np.array(image,dtype=float)

    if arr.ndim != 3 or arr.shape[0] == 0 or arr.shape[1] == 0 or arr.shape[2] != 3:
        return -1
    
    if np.any(arr<0) or np.any(arr>255):
        return -1

    gray = 0.299 * arr[:,:,0] + 0.587 * arr[:,:,1] + 0.114 * arr[:,:,2]
    gray = np.round(gray).astype(int)

    return gray.tolist()

    