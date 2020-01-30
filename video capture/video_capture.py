import cv2, time

# Select video source: 0 (default camera source)
video=cv2.VideoCapture(0)

# Variable to count the number of captured frames
a=0

while True:
    # Every While True loop that occurs will increase the value of 'a' by 1
    a = a+1 

    # Check this video output, and read the frame
    check, frame = video.read()

    print(check)
    print(frame)

    # Convert the frame to grey scale
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Show the frame
    cv2.imshow("Capturing",gray)

    # Each captured frame will be captured for 1ms
    '''Using a while True loop will continuously 
    capture frames for 1ms and create a stream of 
    pictures. Hence, forming a video.''' 
    exit_key = cv2.waitKey(1)

    # Break the video feed if 'q' key is triggered
        # The key objects will accept a unicode character value
            # ord() converts 1 string arguement to a unicode value
    if exit_key == ord('q'):
        break

# Print the total number of frames captured within the video
print(a)
# Once the video display is terminated, release the video capture
video.release()
# Close all of the windows
cv2.destroyAllWindows

