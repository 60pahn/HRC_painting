import cv2
import numpy as np
from cv2 import moments
import math

from skimage.measure import label, regionprops, regionprops_table
import pandas as pd

def getAngle(ax, ay, bx, by, cx, cy):
    ang = math.degrees(math.atan2(cy-by, cx-bx) - math.atan2(ay-by, ax-bx))
    return ang + 360 if ang < 0 else ang



IMG = cv2.imread("Image-Processing/Color region/test-04.png")


print(type(IMG))

np_img1 = np.zeros([200,200,3])
np_img3 = np.zeros([400,400])
np_img = np.zeros([200,200,3])
np_img[slice(40,100),slice(40,100),slice(0,3)]=1

np_img3[slice(40,100),slice(40,100)]=1

np_label = label(np_img3)
prop = regionprops(np_label)
print(type(np_img3))

M = cv2.moments(np_img3)
cX = int(M["m10"] / M["m00"])
cY = int(M["m01"] / M["m00"])

cv2.circle(np_img3, (cX, cY), 20, (.30, .20, .50), 1)


np_img3[cX,cY]=0.5

b_lower = np.array([0,0,0])
b_upper = np.array([255,100,100])
blue_mask=cv2.inRange(IMG, b_lower, b_upper)
#cv2.imshow("blue_mask", blue_mask)

r_lower = np.array([0,0,0])
r_upper = np.array([100,100,255])
red_mask=cv2.inRange(IMG, r_lower, r_upper)
#cv2.imshow("red_mask", red_mask)

g_lower = np.array([0,0,0])
g_upper = np.array([100,255,100])
green_mask=cv2.inRange(IMG, g_lower, g_upper)
#cv2.imshow("green_mask", green_mask)


def centroid(IMG):
    M = cv2.moments(IMG)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    return (cX,cY)

bcx, bcy = centroid(blue_mask)
gcx, gcy = centroid(green_mask)
rcx, rcy = centroid(red_mask)

cv2.circle(IMG, (bcx, bcy), 10, (.30, .20, .50), 1)
cv2.circle(IMG, (rcx, rcy), 10, (.30, .20, .50), 1)
cv2.circle(IMG, (gcx, gcy), 10, (.30, .20, .50), 1)

cv2.line(IMG,(bcx,bcy),(gcx,gcy),(130,130,130),1)
cv2.line(IMG,(gcx,gcy),(rcx,rcy),(130,130,130),1)
cv2.line(IMG,(rcx,rcy),(bcx,bcy),(130,130,130),1)

cv2.putText(IMG, "blue_centroid", (bcx - 25, bcy - 25),cv2.FONT_HERSHEY_PLAIN, 1, (25, 25, 25), 1)
cv2.putText(IMG, "green_centroid", (gcx - 25, gcy - 25),cv2.FONT_HERSHEY_PLAIN, 1, (25, 25, 25), 1)
cv2.putText(IMG, "red_centroid", (rcx - 25, rcy - 25),cv2.FONT_HERSHEY_PLAIN, 1, (25, 25, 25), 1)

print("blue_angle:")
b_a = getAngle(rcx,rcy,bcx,bcy,gcx,gcy)
print(b_a)
print("green_angle:")
g_a = getAngle(bcx,bcy,gcx,gcy,rcx,rcy)
print(g_a)
print("red_angle:")
r_a = getAngle(gcx,gcy,rcx,rcy,bcx,bcy)
print(r_a)
print("sum:")
print(r_a + b_a + g_a)


#cv2.imshow("Image", np_img3)
#cv2.waitKey(0)
cv2.imshow("4", IMG)
cv2.waitKey(0)




#print(prop)
#pd.DataFrame(prop)


#cv2.imshow("3", np_img1)

#HSV = cv2.cvtColor(IMG, cv2.COLOR_BGR2HSV)

#lower = np.array([0,0,0])
#upper = np.array([255,100,100])

#mask = cv2.inRange(IMG, lower, upper)

#cv2.imshow("2", mask)

#cv2.waitKey(0)
#cv2.destroyAllWindows()
