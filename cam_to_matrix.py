#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created May 23, 2015
raspberry pi camera to ht1632-c utility
author: crocdialer@gmail.com
'''

import ht1632c, cv2, picamera, time, random
from picamera.array import PiRGBArray

WIDTH = 24
HEIGHT = 16
COLOR = 1

CAM_IMG_SIZE = (640, 480)
MATRIX_BORDER = (100, 50)

def convert_coords(x, y):
  panel_index = x / 8 + 3 * (y / 8)
  panel_index = 5 - panel_index 
  panel_x =  7 - y % 8
  panel_y = 7 - x % 8
  new_x = panel_index % 3 * 8 + panel_x 
  new_y = panel_index / 3 * 8 + panel_y
  return (new_x, new_y)

class App(object):
  def __init__(self):
    self.led_matrix = ht1632c.HT1632C(1, 0)
    self.cam = picamera.PiCamera()
    self.cam.resolution = CAM_IMG_SIZE 
    self.cam.framerate = 15
    self.raw_capture = PiRGBArray(self.cam, size=CAM_IMG_SIZE)
    self.running = False

  def run(self):
    
    self.running = True
    time.sleep(0.1)
    #while self.running:
    for frame in self.cam.capture_continuous(self.raw_capture, format = 'bgr', use_video_port=True):

      try:

        image = frame.array
        
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        tmp_img = gray
        thresh_val, tmp_img = cv2.threshold(tmp_img, 60, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

        # post processing for LED-matrix image
        tmp_img = cv2.blur(tmp_img, (3, 3))      
  
        # show debug view
        cv2.imshow("pupu", tmp_img)
        cv2.waitKey(1)

        tmp_img = cv2.resize(tmp_img[MATRIX_BORDER[1]:-MATRIX_BORDER[1], MATRIX_BORDER[0]:-MATRIX_BORDER[0]], (WIDTH, HEIGHT))

        self.led_matrix.clear()

        for y in range(0, HEIGHT):
         for x in range(0, WIDTH):
            matrix_x, matrix_y = convert_coords(x, y)
            val = 0 if tmp_img[y, x] == 0 else 1
            self.led_matrix.plot(matrix_x, matrix_y, val)
       
        #self.led_matrix.sendframe()

        #self.led_matrix.clear()
        #for y in range(0, HEIGHT):
        #  for x in range(0, WIDTH):
        #    matrix_x, matrix_y = convert_coords(x, y)
        #    self.led_matrix.plot(matrix_x, matrix_y, 1)
        #    time.sleep(.03)
        #    self.led_matrix.sendframe()
        
        #sz = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
        #self.led_matrix.box(0, 0, sz[0], sz[1], 1)
        
        self.led_matrix.sendframe()
        #print("sendframe")
        
        # clear frame
        self.raw_capture.truncate(0)
        #time.sleep(.5)

      except KeyboardInterrupt:
        print("\nkeyboard interrupt")
        self.cam.close()
        self.led_matrix.close()
        self.running = False
        break

##########################################################################

if __name__ == '__main__':
  print(__doc__)
  App().run()
  print("\nthat's it, that's all")
