'''
Cascades which are stored as .xml files
contain information about the features that 
an image of a face contains.

It takes into consideration all the significant
features, such as the ratio of the eyes, nose and 
lips pixel intensity

Sample images are used to train a model, to label
the images as faces.

Sample Harr cascades: github.com/Itseez/opencv/tree/master/data/haarcascades
'''
import cv2

# Create a face cascade object 
face_cascade = cv2.CascadeClassifier("Files/haarcascade_frontalface_default.xml")

# Load the image
img = cv2.imread("photo.jpg")

# Convert to grayscale as this increases the accuracy of the search
    # By reducing the number fo features that could possibily cause false readings
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Search for the classifier object within the input file
    # Output the coordinates of the detected classifer-object (face) [x,y,width,height]
        # The origin is from the top-right of the detected face
faces=face_cascade.detectMultiScale(gray_img, scaleFactor=1.6, minNeighbors=5)

print(type(faces))
print(faces)

# Draw a rectangle than most closely encompasses the classifier object (the face
    # 1st arg: the img to draw the rectangle on
    # 2nd arg: Top left corner 
    # 3rd arg: Bottom right corner
    # 4th arg: Color (BGR)
    # 5th arg: rectangle-line width
for x, y, w, h in faces:
    img = cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 6)

cv2.imshow("Gray", img)
cv2.waitKey(0)
cv2.destroyAllWindows()