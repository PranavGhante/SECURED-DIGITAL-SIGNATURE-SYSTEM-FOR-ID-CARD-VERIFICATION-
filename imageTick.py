import socket
import cv2
import struct
import pickle
import matplotlib.pyplot as plt
import numpy as np

# Read the image
my_img = cv2.imread("final_id.png")
my_tick = cv2.imread("tick.jpg")

row, col = my_tick.shape[0], my_tick.shape[1]

green = []
tick_r = 72
tick_g = 173
tick_b = 65

for i in range(row):
    for j in range(col):
        r, g, b = my_tick[i][j]
        if g == 173:
            green.append([i, j])

print(len(green))
for i in range(len(green)):
    val = green[i]
    my_img[val[0] + 300][val[1] + 650] = [tick_r, tick_g, tick_b]

# Set the pixel values for the tick at position (600, 400)
tick_length = 50  # Adjust this value as needed
tick_thickness = 5  # Adjust this value as needed


# Display the modified image
plt.imshow(cv2.cvtColor(my_img, cv2.COLOR_BGR2RGB))
plt.title("Image with Tick at (600, 400)")
plt.show()
