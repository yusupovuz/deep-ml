
def calculate_brightness(img):
    sums = 0
    d = 0

    if len(img) < 1:
        return -1
    
    l = len(img[0])

    for i in img:
        for j in i:
            if j > 255 or j < 0:
                return -1
            if l != len(i):
                return -1
            sums += j
            d+=1
    return sums/d