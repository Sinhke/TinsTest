# import cv2
# import numpy as np

# # Đọc hình ảnh
# image = cv2.imread('./Images/Tin/242.b0.1.20250108_frame0000198_obj_1.png', cv2.IMREAD_GRAYSCALE)

# # Khởi tạo SimpleBlobDetector
# detector = cv2.SimpleBlobDetector_create()

# # Phát hiện BLOBs
# keypoints = detector.detect(image)

# # Vẽ BLOBs trên hình ảnh
# im_with_keypoints = cv2.drawKeypoints(image, keypoints, np.array([]), (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# # Hiển thị hình ảnh
# cv2.imshow("BLOBs", im_with_keypoints)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

import cv2
import os

os.listdir('./Images/Tin')


# Read the original image
img = cv2.imread('./Images/Tin/242.b0.1.20250108_frame0000198_obj_1.png') 
# Display original image
cv2.imshow('Original', img)
 
# Convert to graycsale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Blur the image for better edge detection
img_blur = cv2.GaussianBlur(img_gray, (5,5), 0) 
 
# Canny Edge Detection
edges = cv2.Canny(image=img_blur, threshold1=50, threshold2=200) # Canny Edge Detection
# Display Canny Edge Detection Image
cv2.imshow('Canny Edge Detection', edges)
cv2.waitKey(0)
 
cv2.destroyAllWindows()