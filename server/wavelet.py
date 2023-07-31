import numpy as np
import pywt
import cv2


def w2d(img, mode='haar', level=1):
    imarray = img
    # Datatype conversions
    # convert to grayscale
    imarray = cv2.cvtColor(imarray, cv2.COLOR_RGB2GRAY)
    # convert to float
    imarray = np.float32(imarray)
    imarray /= 255;
    # compute coefficients
    coeffs = pywt.wavedec2(imarray, mode, level=level)

    # Process Coefficients
    coeffs_h = list(coeffs)
    coeffs_h[0] *= 0;

    # reconstruction
    im_array_h = pywt.waverec2(coeffs_h, mode);
    im_array_h *= 255;
    im_array_h = np.uint8(im_array_h)

    return im_array_h
