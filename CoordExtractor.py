import cv2
import os
import numpy as np

imPath = "PATH"
pos = [0,0,0,0]

num = len(os.listdir(imPath))
Y = np.zeros((num, 4))

def two_point_recollector():
    for n, f in enumerate(os.listdir(imPath)):
        print(f)
        vid = cv2.VideoCapture(imPath + f)
        b, frame = vid.read()
        width, height, dim = np.array(frame).shape
        print(f"{width}, {height}")
        img = frame.copy()
        cv2.imshow("img", img)

        def afterCheck(event, x, y, flags, userdata):
            if event == cv2.EVENT_MOUSEWHEEL:
                print("Repeating...")
                cv2.imshow("img", img)
                cv2.setMouseCallback("img", on_mouse=call)
            elif event == cv2.EVENT_RBUTTONDOWN:
                print(f"Confirmed -> pt1: ({pos[0]}, {pos[1]}), pt2: ({pos[2]}, {pos[3]})")
                Y[n] = [pos[0], pos[1], pos[2], pos[3]]
                np.savetxt("Y.csv", Y, delimiter=",")
                cv2.destroyAllWindows()

        def call2(event, x, y, flags, userdata):
            if event == cv2.EVENT_MOUSEMOVE:
                img = frame.copy()
                cv2.rectangle(img,
                              (pos[0], pos[1]),
                              (x, y),
                              (0, 255, 0),
                              thickness=3)

                print(f"X: {x}, Y:{y}")
                cv2.imshow("img", img)
            elif event == cv2.EVENT_LBUTTONDOWN:
                print("Done!")
                pos[2] = x
                pos[3] = y
                img = frame.copy()
                cv2.setMouseCallback("img", on_mouse=afterCheck)

        def call(event, x, y, flags, userdata):
            if event == cv2.EVENT_LBUTTONDOWN:
                pos[0] = x
                pos[1] = y
                print(pos)
                cv2.setMouseCallback("img", on_mouse=call2)

        cv2.setMouseCallback("img", on_mouse=call)
        cv2.waitKey(0)

def four_point_recollector():
    for n, f in enumerate(os.listdir(imPath)):
        print(f)
        vid = cv2.VideoCapture(imPath + f)
        b, frame = vid.read()
        width, height, dim = np.array(frame).shape
        print(f"{width}, {height}")
        img = frame.copy()
        cv2.imshow("img", img)

        def afterCheck(event, x, y, flags, userdata):
            if event == cv2.EVENT_MOUSEWHEEL:
                print("Repeating...")
                cv2.imshow("img", img)
                cv2.setMouseCallback("img", on_mouse=x_first)
            elif event == cv2.EVENT_RBUTTONDOWN:
                print(f"Confirmed -> pt1: ({pos[0]}, {pos[1]}), pt2: ({pos[2]}, {pos[3]})")
                Y[n] = [pos[0], pos[1], pos[2], pos[3]]
                np.savetxt("Y.csv", Y, delimiter=",")
                cv2.destroyAllWindows()

        def y_last(event, x, y, flags, userdata):
            if event == cv2.EVENT_MOUSEMOVE:
                im = img.copy()
                im = cv2.rectangle(im, (pos[0], pos[1]), (pos[2], y), (0,255,0), thickness=3)
                im = cv2.circle(im, (pos[0], pos[1]), 4, (255, 0, 0), thickness=5)
                im = cv2.circle(im, (pos[2], y), 4, (0, 0, 255), thickness=5)
                cv2.imshow("img", im)
                print(f"Current: ({pos[2]},{y})")
            elif event == cv2.EVENT_LBUTTONDOWN:
                pos[3] = y
                cv2.setMouseCallback("img",afterCheck)

        def y_first(event, x, y, flags, userdata):
            if event == cv2.EVENT_LBUTTONDOWN:
                pos[1] = y
                cv2.setMouseCallback("img", on_mouse=y_last)

        def x_last(event, x, y, flags, userdata):
            if event == cv2.EVENT_MOUSEMOVE:
                im = img.copy()
                im = cv2.line(im, (pos[0],pos[1]), (x,pos[1]),(0,255,0), thickness=3)
                im = cv2.circle(im, (pos[0], pos[1]), 4,(255,0,0), thickness=5)
                cv2.imshow("img", im)
            elif event == cv2.EVENT_LBUTTONDOWN:
                pos[2] = x
                cv2.setMouseCallback("img", on_mouse=y_first)
        def x_first(event, x, y, flags, userdata):
            if event == cv2.EVENT_LBUTTONDOWN:
                pos[0] = x
                pos[1] = y
                print(pos)
                cv2.setMouseCallback("img", on_mouse=x_last)

        cv2.setMouseCallback("img", on_mouse=x_first)
        cv2.waitKey(0)
four_point_recollector()