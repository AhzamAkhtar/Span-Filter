#pip intall opencv-contrib-python
# pip install czone
#import cv2 as cv
#import cvzone
#APPLYING FILTER ON IMAGES
'''bg=cv.imread("jkr.png")
sunglases=cv.imread("star.png",cv.IMREAD_UNCHANGED)
final=cvzone.overlayPNG(bg,sunglases,[100,100])
cv.imshow("dude",final)
cv.waitKey(0)'''

# APPLYING FILTER ON VIDEOS
import cv2 as cv
import cvzone
capture=cv.VideoCapture(0)
cascade=cv.CascadeClassifier("haarcascade_frontalface_default.xml")
overlay=cv.imread("cool.png",cv.IMREAD_UNCHANGED)
while True:
    ret,frame=capture.read()
    gray=cv.cvtColor(frame,cv.COLOR_RGB2GRAY)
    face=cascade.detectMultiScale(gray)
    for (x,y,w,h) in face:
        #cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        overlay_resize=cv.resize(overlay,(int(w*1.5),int(h*1.5)))
        frame=cvzone.overlayPNG(frame,overlay_resize,[x-45,y-75])
        cv.imwrite("filter.png",frame)
    cv.imshow("dude",frame)

    if cv.waitKey(10) == ord("q"):
        break
cv.destroyAllWindows()
