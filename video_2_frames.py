# -*- coding: utf-8 -*-
"""Video_2_frames.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fc_8hA3Hv9vt3OK1SdXk2AIF8e5O41dr
"""

import cv2
from google.colab import drive

drive.mount('/content/drive')

video_path = '/content/drive/MyDrive/Daily Practice/Single_V_to_F/video2.mp4'

video = cv2.VideoCapture(video_path)
success = True
count = 1
while success:
  success,frame = video.read()
  name = '/content/drive/MyDrive/Daily Practice/Single_V_to_F/Extracted Frames/'+str(count)+'.jpg'
  if success == True:
    cv2.imwrite(name,frame)
    print('Frame {} Extracted Successfully'.format(count))
    count = count+1
  else:
    break