#Step 1: Use youtube-dl in command line. The exact thing to type is
#youtube-dl *youtube link here without any quotes or asterisk or anything*
#This will download the youtube video into the folder with this code
#The folder is C:\Users\Penguin\Coding stuff\Youtube to Bass Tab
#Get rid of apostrophes in the file title just for sake of ease

#Step 2: Using openCV to take pictures of every video frame
import cv2
import numpy 
import os

vidcap = cv2.VideoCapture('myvid.mp4')
success,image = vidcap.read()
print(success, image)
count = 0
while success:
  cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1

#Step 3: Crop all the frames to just include the tab
for i in range(count):
    pic = f'frame{i}.jpg'
    img = cv2.imread(pic)
    cropped_image = img[0:120,:] # Slicing to crop the image
    

#Step LAST: Once we are done with all the frames we need to delete all the files
#Count tells us how many files there are
for i in range(count):
    os.remove(f'frame{i}.jpg')

print('Done master Jacob uwu owo')






#THE PLAN IS AS FOLLOWS:
#1 - download a youtube video that shows bass tab that I wish to learn - DONE
#2 - take pictures of all of the times that the tab changes in youtube video -> take pictures every frame - DONE
#2.5 - crop the pictures to only include the tab
#2.75 - identify which pictures are duplicates and can be removed 
#3 - put all of those pictures together into a tab document that I can then print 