import cv2
import matplotlib.pyplot as plt
import imutils

phone = cv2.imread("photos/iphone-holding.jpg")
phone = cv2.cvtColor(phone, cv2.COLOR_BGR2RGB)
h, w, _ = phone.shape

app = cv2.imread("photos/figma-design.png")
app = cv2.cvtColor(app, cv2.COLOR_BGR2RGB)
smaller_app = cv2.resize(app, (200, 370))
rotated_app = imutils.rotate_bound(smaller_app, 1.0)
hh, ww, _ = rotated_app.shape

yoff = round((h - hh)/2) - 20
xoff = round((w - ww)/2) - 95
print(yoff ,xoff)
result = phone.copy()
result[yoff:yoff+hh, xoff:xoff+ww] = rotated_app

plt.imshow(result)
plt.axis('off')
plt.savefig("photos/final-phone.png", bbox_inches='tight', pad_inches=0)