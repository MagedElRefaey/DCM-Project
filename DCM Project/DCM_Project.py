# -*- coding: utf-8 -*-
"""biomedical data assignment n0.4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BeB0rTAbMoJZ3SJfOLLslbeWxGQDxmJT
"""

!pip install pydicom

import pydicom

from pydicom import dcmread

import pydicom.data

path=r"/content"

file_name="00000002.dcm"

file=pydicom.data.data_manager.get_files(path,file_name)[0]

ds=pydicom.dcmread(file)

print(ds)

type(ds)

ds[0x0010,0x0010]

# changing patient name

ds[0x0010,0x0010].value="abdeen"

ds[0x0010,0x0010]

ds[0x0010,0x0020]

ds[0x0010,0x0020].value="19106051"

ds[0x0010,0x0020]

ds[0x0008,0x0060]

ds[0x0008,0x0070]

ds[0x0008,0x1050]

#changing pysician's name

ds[0x0008,0x1050].value="mohammed"

ds[0x0008,0x1050]

ds[0x0008,0x0020]

#reshaping date

ds[0x0008,0x0020].value="2021/02/26"

ds[0x0008,0x0020]

ds[0x0032,0x0032].value="2021/02/26"

ds[0x0032,0x0032]

ds[0x0008,0x2111]

ds[0x0029,0x1030]

ds[0x2010,0x0040]

ds[0x0028,0x0002]

ds[0x0028,0x0030]

ds[0x0028,0x0010],ds[0x0028,0x0011]

import matplotlib.pyplot as plt

plt.imshow(ds.pixel_array,cmap='bone')

pip install pillow

from PIL import Image

pip install numpy

import numpy as np

#now extracting the pixels from file and turn type to float so we don't lose information

image=ds.pixel_array.astype(float)

#change the size into 0,255

image2=(np.maximum(image,0)/image.max()) *255.0

#changing image to 8 bits unsigned integer

image2=np.uint8(image2)

# creating image fromm array

image3=Image.fromarray(image2)

# show image

image3.show()

#save image as jpg

image3.save('00000002.jpg')

#save image as png

image3.save('00000002.png')