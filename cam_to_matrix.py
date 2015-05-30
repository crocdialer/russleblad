#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created May 23, 2015
raspberry pi camera to ht1632-c utility
author: crocdialer@gmail.com
'''

import ht1632c, cv2, picamera, time, random

WIDTH = 24
HEIGHT = 16
COLOR = 1

class App(object):
  def __init__(self):
    self.led_matrix = ht1632c.HT1632C(1, False)
    #self.cam = picamera.PiCamera()
    self.running = False

  def run(self):

    self.running = True
    while self.running:
    
      try:
        self.led_matrix.clear()

        #for x in range(0, WIDTH):
        #  for y in range(0, HEIGHT):
        #    self.led_matrix.plot(x, y, 1)
        #    time.sleep(.33)
        #    self.led_matrix.sendframe()
       
        #for x in range(0, WIDTH):
        #  for y in range(0, HEIGHT):
        #    self.led_matrix.plot(x, y, 0)
        #    time.sleep(.33)
        #    self.led_matrix.sendframe()
        
        sz = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
        self.led_matrix.box(0, 0, sz[0], sz[1], 1)
        
        self.led_matrix.sendframe()
        #print("sendframe")
        time.sleep(.15)

      except KeyboardInterrupt:
        print("\nkeyboard interrupt")
        self.led_matrix.close()
        self.running = False

##########################################################################

if __name__ == '__main__':
  print(__doc__)
  App().run()
  print("\nthat's it, that's all")
