import cv2
import pickle
import matplotlib.pyplot as plt
import hashlib

my_img = cv2.imread("tejas.jpeg")

# Display the original image
plt.imshow(cv2.cvtColor(my_img, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.show()


face = [[0 for x in range(400)] for y in range(400)]

print(len(my_img[0]))
for i in range(211, 561):
    for j in range(130, 486):
        face[i - 211][j - 130] = my_img[i][j]

bytes_face = pickle.dumps(face)

# Compute the SHA-256 hash
hash_object = hashlib.sha256(bytes_face)
hex_dig = hash_object.hexdigest()

print("SHA-256 hash of the list 'face':", hex_dig)
