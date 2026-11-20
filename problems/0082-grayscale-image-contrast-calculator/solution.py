import numpy as np

def calculate_contrast(img) -> int:
    """
    Calculate the contrast of a grayscale image.
    Args:
        img (numpy.ndarray): 2D array representing a grayscale image with pixel values between 0 and 255.
    """
    # Your code here
    minx = 1000000
    maxx = -999999
    for i in img:
        for j in i:
            if minx > j:
                minx = j
            if maxx < j:
                maxx = j
    return maxx - minx