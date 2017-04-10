import cv2
import numpy as np

def nothing(x):
    pass

# Create a black image, a window
control = np.zeros((100,100,3),np.uint8)
print control
cv2.namedWindow('Control')
img = np.zeros((600,600,3),np.uint8)
cv2.namedWindow('Paint')
# create trackbars for color change
cv2.createTrackbar('R','Control',0,255,nothing)
cv2.createTrackbar('G','Control',0,255,nothing)
cv2.createTrackbar('B','Control',0,255,nothing)
cv2.createTrackbar('WThickness','Control',1,6,nothing)
cv2.createTrackbar('DThickness','Control',5,50,nothing)
ix,iy=[0,0]
drawing = False
def draw_paint(event,x,y,flags,param):
    global ix,iy,drawing,s
    # get current positions of four trackbars
    r = cv2.getTrackbarPos('R','Control')
    g = cv2.getTrackbarPos('G','Control')
    b = cv2.getTrackbarPos('B','Control')
    rt = cv2.getTrackbarPos('WThickness','Control')
    dt = cv2.getTrackbarPos('DThickness','Control')
    s = cv2.getTrackbarPos(switch,'Control')

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            ix,iy = x,y
            if s == 1:
                cv2.circle(img,(ix,iy),rt,(r,g,b),-1)
            else:
                cv2.circle(img,(ix,iy),dt,(255,255,255),-1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False

# create switch for ON/OFF functionality
switch = '0 : Erase \n1 : Write'
cv2.createTrackbar(switch,'Control',0,1,nothing)
cv2.setMouseCallback('Paint',draw_paint)
img[:] = [255,255,255]
color_img = np.zeros((50,100,3),np.uint8)
while(1):
    color_img[:] = [cv2.getTrackbarPos('R','Control'),cv2.getTrackbarPos('G','Control'),cv2.getTrackbarPos('B','Control')]
    cv2.imshow('Control',color_img)
    cv2.imshow('Paint',img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        break

cv2.destroyAllWindows()