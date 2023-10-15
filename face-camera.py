import cv2

# Initialize the VideoCapture object (0 for the default camera)
cap = cv2.VideoCapture(0)

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
else:
    # Capture a frame from the camera
    ret, frame = cap.read()

    # Check if the frame is captured successfully
    if ret:
        # Display the captured frame (optional)
        cv2.imshow('Captured Image', frame)
        
        # Save the captured frame as an image file
        cv2.imwrite('captured_photo.jpg', frame)
        print("Image captured and saved as 'captured_photo.jpg'.")
    else:
        print("Error: Could not capture frame from the camera.")

    # Release the camera and close the window after a key press
    cap.release()
    cv2.waitKey(3)
    cv2.destroyAllWindows(4)
