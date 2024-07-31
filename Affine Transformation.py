import cv2
import matplotlib.pyplot as plt
import numpy as np
img= cv2.imread("C:/Users/singh/OneDrive/Pictures/cherry blossom.jpg")
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
rows, cols, channels = img_rgb.shape
ptsl= np.float32([[50,50], [200,50],[50,200]])
pts2 =np.float32([[10,100],[200,50],[100,250]])
M= cv2.getAffineTransform(ptsl,pts2)
dst = cv2.warpAffine(img_rgb,M,(cols,rows))
plt.subplot(121), plt.imshow(img_rgb), plt.title('Original Image')
plt.subplot(122), plt.imshow(dst), plt.title('Output Image')
plt.show()