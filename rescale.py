import cv2 as cv

# resizing and rescaling is helpful to get
# rid of unecessary data, similar to compression imo
# reduces computation time significantly


def rescale_frame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

cap = cv.VideoCapture('videos/dog.mp4')

while True:
    # reads in each frame
    isTrue, frame = cap.read()

    frame_resized = rescale_frame(frame, scale=0.2)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('q'):
        break

cap.release()

cv.destroyAllWindows()

cv.waitKey(0)

cv.waitKey(0)