import numpy as np
import cv2


# read
def kelimecevir(a):
    img = cv2.imread(a, cv2.IMREAD_GRAYSCALE)

    # increase contrast
    pxmin = np.min(img)
    pxmax = np.max(img)
    imgContrast = (img - pxmin) / (pxmax - pxmin) * 255

    # increase line width
    kernel = np.ones((3, 3), np.uint8)
    imgMorph = cv2.erode(imgContrast, kernel, iterations = 1)

    # write
    cv2.imwrite('kc.png', imgMorph)
    resim="kc.png"
    return resim
    

def paragrafcevir(b):
    img = cv2.imread(b)

    alpha=2
    beta=50

    result=cv2.addWeighted(img, alpha , np.zeros(img.shape, img.dtype), 0, beta)
    gri = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
    thresh1 = cv2.adaptiveThreshold(gri, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 
                                          cv2.THRESH_BINARY, 199, 5) 

    cv2.imwrite('test.png',thresh1)
    resim2="test.png"
    return resim2


