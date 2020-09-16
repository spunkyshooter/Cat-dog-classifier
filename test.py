from utils import predict , load 
import matplotlib.pyplot as plt
import numpy as np
import cv2

parameters = load("parameters")
classes = load("classes")

num_px = 64

fname= "cat1.jpg" # change this to the name of image file 
my_label_y = [1] # the true class of your image (1 -> cat, 0 -> non-cat)


image = cv2.imread(fname)
my_image = cv2.resize(image, (num_px,num_px), interpolation = cv2.INTER_AREA).reshape((num_px*num_px*3,1))
my_image = my_image/255.
my_predicted_image = predict(my_image, my_label_y, parameters)

plt.imshow(image)
print ("y = " + str(np.squeeze(my_predicted_image)) + ", your L-layer model predicts a \"" + classes[int(np.squeeze(my_predicted_image)),].decode("utf-8") +  "\" picture.")

plt.show()
