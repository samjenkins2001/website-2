import numpy as np
import matplotlib.pyplot as plt
import cv2

image = cv2.imread("photos/myface.JPG")
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
h,w = image_gray.shape
print('Image Dimensions: height={}, width={}'.format(h, w))
background = np.where(image_gray > 200, 0, 255)
uint8_background = np.uint8(background)

mask1 = np.zeros_like(image_gray)
mask1[:, :] = [255]
start_point = ((0),(1110))
end_point = ((270),(1300))
color = (0)
mask = cv2.rectangle(mask1, start_point, end_point, color, -1)
result1 = cv2.bitwise_and(uint8_background, mask)

mask2 = np.zeros_like(result1)
mask2[:, :] = [255]
start_point = ((775),(850))
end_point = ((1008),(1300))
color = (0)
mask = cv2.rectangle(mask2, start_point, end_point, color, -1)
result2 = cv2.bitwise_and(result1, mask)

mask3 = np.zeros_like(result2)
mask3[:, :] = [255]
start_point = ((775),(400))
end_point = ((1008),(800))
color = (0)
mask = cv2.rectangle(mask3, start_point, end_point, color, -1)
result3 = cv2.bitwise_and(result2, mask)

mask4 = np.zeros_like(result3)
mask4[:, :] = [255]
start_point = ((0),(0))
end_point = ((1008),(300))
color = (0)
mask = cv2.rectangle(mask4, start_point, end_point, color, -1)
result4 = cv2.bitwise_and(result3, mask)

mask5 = np.zeros_like(result4)
mask5[:, :] = [255]
start_point = ((0),(400))
end_point = ((185),(1320))
color = (0)
mask = cv2.rectangle(mask5, start_point, end_point, color, -1)
result5 = cv2.bitwise_and(result4, mask)

font = cv2.FONT_HERSHEY_COMPLEX
font_size = 4
font_color = 0
font_thickness = 2
text = 'person'
img_text = cv2.putText(result5, text, (250, 1600), font, font_size, font_color, font_thickness, cv2.LINE_AA)

font = cv2.FONT_HERSHEY_COMPLEX
font_size = 4
font_color = 255
font_thickness = 2
text = 'background'
img_text = cv2.putText(result5, text, (100, 300), font, font_size, font_color, font_thickness, cv2.LINE_AA)

plt.imshow(img_text)
plt.axis('off')
plt.savefig("photos/mask.png", bbox_inches='tight', pad_inches=0)