import sys, cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
class Coins:
    summ=0
    def addcoin(self, r):
        if r>82:
            value=5
            self.summ=self.summ+5
        elif 75<=r<=82:
            value=2
            self.summ=self.summ+2
        elif r<75:
            value=1
            self.summ=self.summ+1
        return value

img = cv.imread('5.jpg', 1)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray = cv.GaussianBlur(gray, (7, 7), 0.5) 
#edges = cv.Canny(gray, 0, 50)
circles = cv.HoughCircles(gray,cv.HOUGH_GRADIENT,1,120,
                            param1=200,param2=35,minRadius=60,maxRadius=100)
#circles = np.uint16(np.around(circles))
money = Coins()
for i in circles[0,:]:
    # draw the outer circle
    cv.circle(img, (i[0], i[1]), i[2], (0,255,0), 2)
    # draw the center of the circle
    cv.circle(img, (i[0], i[1]), 2, (0,0,255), 3)

    v = money.addcoin(i[2])

    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(img, str(v), (i[0],i[1]), font, 2, (255,0,0), 2, cv.LINE_AA)

cv.putText(img, str(money.summ), (50,100), font, 2, (255,255,0), 2, 			cv.LINE_AA)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')

plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()