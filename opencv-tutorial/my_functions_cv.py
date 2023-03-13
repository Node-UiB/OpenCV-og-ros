import cv2 as cv

class Cv_functions():
    def __init__(self) -> None:
        pass

    def displayImg(img_path):
        img = cv.imread(img_path)

        cv.imshow('balls', img)

        cv.waitKey(0)
    
    def displayVid(vid_path = ''):
        capture = cv.VideoCapture(vid_path) #Takes an integer for webcams, or a path for a video

        while True:
            isTrue, frame = capture.read() #Returns bool for if the frame has been read, and the frame
            cv.imshow('video', frame)

            if cv.waitKey(20) & 0xFF == ord('d'):
                break

        capture.release()
        cv.destroyAllWindows()