import cv2 as cv

#Reading img
# img = cv.imread('balls.png')

# cv.imshow('balls', img)

# cv.waitKey(0)

#Reading video

capture = cv.VideoCapture('opencv-tutorial/trololol.mp4') #Takes an integer for webcams, or a path for a video


while True:
    isTrue, frame = capture.read() #Returns bool for if the frame has been read, and the frame
    cv.imshow('video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()