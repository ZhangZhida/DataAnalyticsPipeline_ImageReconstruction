import cv2 
import numpy as np

image = cv2.imread('/home/zhida/Pictures/1__NQN6_YnxS29m8vFzWYlEg.png' )
# image = image_read = open('/home/zhida/Pictures/1__NQN6_YnxS29m8vFzWYlEg.png','rb').read()

img_str = cv2.imencode('.png', image)[1].tostring()
print(type(img_str))

nparr = np.fromstring(img_str, np.uint8)
img2 = cv2.imdecode(nparr, cv2.CV_32FC4)

cv2.imwrite('test.png', img2)

print(type(img2))