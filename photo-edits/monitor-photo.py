import cv2
import matplotlib.pyplot as plt

monitor = cv2.imread("photos/monitor.jpg")
big_monitor = cv2.resize(monitor, (1656, 1154))
print(monitor.shape)
print(big_monitor.shape)
h, w, _ = big_monitor.shape

segmentation = cv2.imread("photos/segmentation.png")
segmentation = cv2.cvtColor(segmentation, cv2.COLOR_BGR2RGB)
smaller_segmentation = cv2.resize(segmentation, (843, 470))
print(segmentation.shape)
print(smaller_segmentation.shape)
hh, ww, _ = smaller_segmentation.shape

yoff = round((h - hh)/2) - 83
xoff = round((w - ww)/2) - 3
print(yoff ,xoff)
result = big_monitor.copy()
result[yoff:yoff+hh, xoff:xoff+ww] = smaller_segmentation

plt.imshow(result)
plt.axis('off')
plt.savefig("photos/final-monitor.png", bbox_inches='tight', pad_inches=0)