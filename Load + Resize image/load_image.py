import cv2

# Load the image
# import in color (2nd arguement: 0=black and white, 1=color, -1:alpha transparency)
img = cv2.imread("galaxy.jpg",1)

# The image is turned in a numpy array
print(type(img))

# The numbers in the first array denote the greyscale intensity of the pixels
    # Along the rows and the columns
print(img)

# The the pixel size of the image (array):
print(img.shape)

# Check the number of dimensions
    # When the 2nd arguement for the .imread method is 0 (black_and_white): 2 dimensional array
    # When the 2nd arguement for the .imread method is 0 (color): 3 dimensional array [r,c,RGB]
print(img.ndim)

# Create a window with a title: "Galaxy", display the image object: img:
cv2.imshow("Galaxy",img)
# Define how long the window should be open for
 # 0 will close the window on next key-press, all other postive values define ms
cv2.waitKey(2000)
# Close all the opened windows (images) after waiting for the defined time
cv2.destroyAllWindows()
