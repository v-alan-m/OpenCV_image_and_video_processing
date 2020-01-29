import cv2

img = cv2.imread("galaxy.jpg",1)

print(type(img))
print(img)
print(img.shape)
print(img.ndim)

# Resize the image
resized_image = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))

# Insert the resized image object to be displayed
cv2.imshow("Galaxy",resized_image)

# Write the new image to a file
cv2.imwrite("Galaxy_resized.png",resized_image)

cv2.waitKey(2000)
cv2.destroyAllWindows()
