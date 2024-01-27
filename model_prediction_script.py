#!/usr/bin/env python
# coding: utf-8

# In[48]:


#get_ipython().system('pip install torch')
#get_ipython().system('pip install ultralytics')
#get_ipython().system('pip install opencv-python')


# In[49]:


from ultralytics import YOLO


# In[58]:


model1=YOLO('last (6).pt')


# In[51]:


import cv2
import matplotlib.pyplot as plt
def display(im_path):
    dpi=80
    im_data=plt.imread(im_path)
    height,width,depth=im_data.shape

    figsize=width/float(dpi), height/float(dpi)

    fig=plt.figure(figsize=figsize)
    ax=fig.add_axes([0,0,1,1])

    ax.axis('off')

    ax.imshow(im_data, cmap='gray')

    plt.show()


# In[53]:


#get_ipython().system('pip install pyfirmata')
# from pyfirmata import Arduino,SERVO,util
# from time import sleep
# port = '/dev/ttyACM0'
# pin = 10
# board = Arduino(port)
# board.digital[pin].mode = SERVO
# def rotateservo(pin,angle):
#     board.digital[pin].write(angle)
#     sleep(0.015)


# In[61]:


from glob import glob
waste_imgs = glob('/home/soumoroy/project_smart_bin_rnd/WhatsApp Image 2024-01-27 at 8.58.24 PM.jpeg')
for img_file in waste_imgs:
    img = cv2.imread(img_file)
    results = model1.predict(conf=0.25, source=img_file, save_crop = True)
    names = model1.names
    display(img_file)
    for r in results:
        for c in r.boxes.cls:
            print(names[int(c)])
            if (names[int(c)]=='plastic'):
                for i in range(0,90):
                    #rotateservo(pin,i)
                    print("90 degree")
            elif (names[int(c)]=='non-plastic'):
                for i in range(0,180):
                    print("180 degree")
                    #rotateservo(pin,i)
            else:
                continue

