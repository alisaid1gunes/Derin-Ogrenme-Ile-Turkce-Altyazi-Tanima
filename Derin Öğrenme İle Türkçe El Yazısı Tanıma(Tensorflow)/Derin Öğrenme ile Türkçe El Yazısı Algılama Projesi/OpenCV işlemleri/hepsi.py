import page
import words
import opncvisle
from PIL import Image
import cv2
import os


a="4.jpg"  # test etmek istedigin resmi gir


if not os.path.exists('segmented/'+a):
	os.makedirs('segmented/'+a)


rsm=opncvisle.kelimecevir(a)
rsm2=opncvisle.paragrafcevir(rsm)

# User input page image 
image = cv2.cvtColor(cv2.imread(rsm2), cv2.COLOR_BGR2RGB)

# Crop image and get bounding boxes
crop = page.detection(image)
boxes = words.detection(crop)
lines = words.sort_words(boxes)

# Saving the bounded words from the page image in sorted way

i = 84074
for line in lines:
    text = crop.copy()
    for (x1, y1, x2, y2) in line:
        # roi = text[y1:y2, x1:x2]
        save = Image.fromarray(text[y1:y2, x1:x2])
        # print(i)
        
        save.save("segmented/"+a+"/"+"sub-sub-"+ str(i) + ".png")
        i += 1
