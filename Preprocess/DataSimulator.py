import cv2
import numpy as np

drawing = False
ix, iy = -1, -1

def draw_line(event, x, y, flags, param):
    global ix, iy, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        # print 'left button down'
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        # print 'mouse move'
        if drawing == True:
            # BGR
            cv2.rectangle(img, (ix, iy), (x, y), (100, 100, 230), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        # print 'left button up'
        drawing = False

img = np.zeros((300, 300, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_line)

picstr = ''
while (True):
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xff
    if k == ord('c'):
        img = np.zeros((300, 300, 3), np.uint8)
        print 'you typed key c, clean canvas!'
    elif k == ord('s'):
        imgname = raw_input('Please input picture name:')
        cv2.imwrite('B' + imgname + '.png', img)
        print 'you typed key s, save image!'
        img = np.zeros((300, 300, 3), np.uint8)
        # break
    elif k == ord('z'):
        print 'you typed key z, exit!'
        break

cv2.destroyAllWindows()

