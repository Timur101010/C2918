import cv2
from PIL import Image

image_path = 'mountain.jpeg'

cat_face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
image = cv2.imread(image_path)

cat_face = cat_face_cascade.detectMultiScale(image)

cat = Image.open(image_path)
glasses = Image.open('human.png')
cat = cat.convert("RGBA")
glasses = glasses.convert("RGBA")

for(x,y,w,h) in cat_face:
    glasses = glasses.resize((w, int(h/3)))
    cat.paste(glasses, (x, int(y + h / 4)), glasses)
    cat.save("man_on_the_mountain.png")
    cat_with_glasses = cv2.imread('man_on_the_mountain.png')


cv2.imshow("man_on_the_mountain", cat_with_glasses)
cv2.waitKey()