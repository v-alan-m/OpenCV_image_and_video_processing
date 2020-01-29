import cv2
import glob

# Create a list 
    # Containing the file-paths to all the .jpg files
images=glob.glob("*.jpg")
print(images)

for image in images:
    img=cv2.imread(image,1)
    re=cv2.resize(img,(100,100))
    cv2.imshow("Hey",re)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    # The name of the resized files will be "Resized_" + the original name 
        # Return True if the image has been saved successfully
            # Add 're' as the 3rd arguement
    cv2.imwrite("resized_images/resized_"+image,re)

