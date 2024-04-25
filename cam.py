# Enumerate available cameras
import cv2
n = int(input("Enter the index limit: "))
for i in range(n):  # Try up to 10 indices
    cap = cv2.VideoCapture(i)
    if cap.isOpened():
        print(f"Camera at index {i} is available")
        cap.release()