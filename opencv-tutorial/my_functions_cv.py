import cv2 as cv

'''
This is a class implementation of various scripts you can create with opencv. They are defined as class methods.  
'''


class Cv_functions():
    def __init__(self) -> None:
        pass

    def displayImg(self, img_path):
        img = cv.imread(img_path)

        cv.imshow('balls', img)

        cv.waitKey(0) #If you want to wait for a specific key, use cv.waithek(0) == ord('key')
        cv.destroyAllWindows()
    
    def displayVid(self, vid_path = ''):
        capture = cv.VideoCapture(vid_path) #Takes an integer for webcams, or a path for a video

        while True:
            isTrue, frame = capture.read() #Returns bool for if the frame has been read, and the frame
            cv.imshow('video', frame)

            if cv.waitKey(20) == ord('d'):# Old implementation "& 0xFF == ord('d')" is unecessary. New implementation does this automatically when wait == ord
                break

        capture.release()
        cv.destroyAllWindows()

        #If you get an error: (-215:Assertion failed), then the video ran out of frames, and can not find more frames.
        #It raises a cv2.error: , so it can break out of the loop.
        #This is the same error as when a wrong path to a video or picture is stated. 

    