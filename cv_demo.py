import cv2
import os
import numpy as np
from skimage.measure import block_reduce
from skimage.io import imread

from keras.models import model_from_json

root_dir='D:/JetBrains_projects/PycharmProjects/work/'
os.chdir(root_dir)

model = model_from_json(open('model.json').read())
model.load_weights('weights.h5')


def print_indicator(data, model, class_names, bar_width=50):
    probabilities = model.predict(np.array([data]))[0]
    #print(probabilities)
    left_count = int(probabilities[1] * bar_width)
    right_count = bar_width - left_count
    left_side = '-' * left_count
    right_side = '-' * right_count
    return class_names[0], left_side + 'XXX' + right_side, class_names[1]

class_names = ['Unhappy', 'Happy']
cap=cv2.VideoCapture(0)

# Check if camera opened successfully
if (cap.isOpened () == False):
    print ("Error opening video stream or file")

# Read until video is completed
while (cap.isOpened ()):
    # Capture frame-by-frame
    ret, frame = cap.read ()
    frame_2_analyze=cv2.resize(frame,dsize=(32,32))
    frame_2_analyze=cv2.cvtColor (frame_2_analyze, cv2.COLOR_BGR2GRAY)

    if ret == True:
        data = frame_2_analyze.astype (np.float) / 255
        data = np.expand_dims (data, axis=2)
        txt=print_indicator (data, model, class_names, bar_width=20)
        print(txt)
        # Display the resulting frame
        cv2.imshow ('CamView', frame)
        # Press Q on keyboard to  exit
        if cv2.waitKey (25) & 0xFF == ord ('q'):
            break

    # Break the loop
    else:
        break

# When everything done, release the video capture object
cap.release ()

# Closes all the frames
cv2.destroyAllWindows()