import numpy as np
import os
from PIL import Image
import StringIO

root_dir = 'D:/JetBrains_projects/PycharmProjects/work/'
os.chdir(root_dir)

f=open('SMILEsmileD-master/SMILEs/negatives/negatives7/10.jpg','rb')

buffer = file("xyz.jpg").read()
si = StringIO.StringIO(buffer)
i = Image.open(si)
i.show()

buf=f.read()
img=Image.open(StringIO.StringIO(f.read()))
img.show()
#print(np.asarray(img))



