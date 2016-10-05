import numpy as np
import cv2
import sys


def calc_sloop_change(histo, mode, tolerance):
   sloop = 0
   for i in range(0, len(histo)):
      if histo[i] > max(1, tolerance):
         sloop = i
         return sloop
      else:
         sloop = i


def process(inpath, outpath, tolerance):
   original_image = cv2.imread(inpath)
   tolerance = int(tolerance) * 0.01

   #Get properties
   width, height, channels = original_image.shape

   color_image = original_image.copy()

   blue_hist = cv2.calcHist([color_image], [0], None, [256], [0, 256])
   green_hist = cv2.calcHist([color_image], [1], None, [256], [0, 256])
   red_hist = cv2.calcHist([color_image], [2], None, [256], [0, 256])

   blue_mode = blue_hist.max()
   blue_tolerance = np.where(blue_hist == blue_mode)[0][0] * tolerance
   green_mode = green_hist.max()
   green_tolerance = np.where(green_hist == green_mode)[0][0] * tolerance
   red_mode = red_hist.max()
   red_tolerance = np.where(red_hist == red_mode)[0][0] * tolerance

   sloop_blue = calc_sloop_change(blue_hist, blue_mode, blue_tolerance)
   sloop_green = calc_sloop_change(green_hist, green_mode, green_tolerance)
   sloop_red = calc_sloop_change(red_hist, red_mode, red_tolerance)

   gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
   gray_hist = cv2.calcHist([original_image], [0], None, [256], [0, 256])

   largest_gray = gray_hist.max()
   threshold_gray = np.where(gray_hist == largest_gray)[0][0]

   #Red cells
   gray_image = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 85, 4)

   _, contours, hierarchy = cv2.findContours(gray_image, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

   c2 = [i for i in contours if cv2.boundingRect(i)[3] > 15]
   cv2.drawContours(color_image, c2, -1, (0, 0, 255), 1)

   cp = [cv2.approxPolyDP(i, 0.015 * cv2.arcLength(i, True), True) for i in c2]

   countRedCells = len(c2)

   for c in cp:
      xc, yc, wc, hc = cv2.boundingRect(c)
      cv2.rectangle(color_image, (xc, yc), (xc + wc, yc + hc), (0, 255, 0), 1)

   #Malaria cells
   gray_image = cv2.inRange(original_image, np.array([sloop_blue, sloop_green, sloop_red]), np.array([255, 255, 255]))

   _, contours, hierarchy = cv2.findContours(gray_image, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

   c2 = [i for i in contours if cv2.boundingRect(i)[3] > 8]
   cv2.drawContours(color_image, c2, -1, (0, 0, 0), 1)

   cp = [cv2.approxPolyDP(i, 0.15 * cv2.arcLength(i, True), True) for i in c2]

   countMalaria = len(c2)

   for c in cp:
      xc, yc, wc, hc = cv2.boundingRect(c)
      cv2.rectangle(color_image, (xc, yc), (xc + wc, yc + hc), (0, 0, 0), 1)

   #Write image
   cv2.imwrite(outpath, color_image)

   #Write statistics
   with open(outpath + '.stats', mode='w') as f:
      f.write(str(countRedCells) + '\n')
      f.write(str(countMalaria) + '\n')


