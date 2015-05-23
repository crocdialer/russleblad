#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created May 23, 2015
raspberry pi camera to ht1632-c utility
author: crocdialer@gmail.com
'''

import ht1632c, cv2, picamera, time

class App(object):
  def __init__(self):
    self.led_matrix = ht1632c.HT1632C(1, False)
    self.cam = picamera.PiCamera()

  def run(self):
    while True:
    
      try:
        pass

      except KeyboardInterrupt:
        print("\nkeyboard interrupt")

##########################################################################

if __name__ == '__main__':
  print(__doc__)
  App().run()
  print("\nthat's it, that's all")
