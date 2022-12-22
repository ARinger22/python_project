import numpy as np
import imageio.v2 as imageio
import cv2
import scipy.ndimage 
import matplotlib.pyplot as plt
fig = plt.figure()

img = 'arp2.jpg'

def grayscale(rgb):
    return np.dot(rgb[...,:3], [0.299,0.587, 0.114]) # 2 dimensional array to convert image to sketch

def dodge(front,back):
    result=front*255/(255-back)
    result[result>255] =255
    result[back==255] = 255
    return result.astype('uint8')

S =imageio.imread(img)
g = grayscale(S)
i=255-g

b= scipy.ndimage.gaussian_filter(i,sigma=10)
r=dodge(b,g)
cv2.imwrite('sketch.png',r)
ax1 = fig.add_subplot(121)  # left side
ax2 = fig.add_subplot(122)
ax1.imshow(r)
plt.show()
