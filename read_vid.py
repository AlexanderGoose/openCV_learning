import cv2 as cv

capture = cv.VideoCapture('videos/dog.mp4')

# to read a video, must use loop to read frame by frame
while True:
    # reads in each frame
    isTrue, frame = capture.read()

    # displays each frame of the video
    cv.imshow('Video', frame)

    # checks for video to be over
    if cv.waitKey(20) & 0xFF==ord('q'):
        break

# when video is fone, must release
capture.release()

# closes all of the opened frames when video is done
cv.destroyAllWindows()

# waits for a key to be pressed
cv.waitKey(0)