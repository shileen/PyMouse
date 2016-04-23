import pyautogui
import cv2
import cv2.cv as cv

#using opencv1.0 functions
camera = cv.CaptureFromCAM(0)

#initializing font, color and variables
font= cv.InitFont(cv.CV_FONT_HERSHEY_SIMPLEX, 0.5, 1, 0, 2, 8)
color = (0, 0, 0)
point1 = (300, 200)
point2 = (400, 300)
flag=0
while True:
        
        #grabbing a frame, applying blur, flipping the image
        frame=cv.QueryFrame(camera)
        cv.Smooth(frame, frame, cv.CV_BLUR, 3)
        cv.Flip(frame, frame, 1)

        #drawing the rectangle and writing the text
        temp1 = cv.CloneImage(frame)
        cv.Rectangle(temp1, point1, point2, color, 1)
        cv.PutText(temp1, "Place in box", (430, 240), font, color)
        cv.PutText(temp1, "then hit q", (430, 260), font, color)

        #taking snapshot after q is pressed
        if cv.WaitKey(10) == 113:
                   flag = 1
                   cv.SetImageROI(temp1, (300, 200, 100, 100))
                   template = cv.CloneImage(temp1)
                   cv.ResetImageROI(temp1)
                   cv.DestroyWindow("Image")
	
        if flag==0:
                   cv.NamedWindow("Image", 1)
                   cv.MoveWindow("Image", 300, 0)
                   cv.ShowImage("Image", temp1)
                   continue

        W, H = cv.GetSize(frame)
        w, h = cv.GetSize(template)

        width = W-w+1
        height = H-h+1
        result = cv.CreateImage((width, height), 32, 1)
        #matching the template by searching for the given region in the image
        cv.MatchTemplate(frame, template, result, cv.CV_TM_SQDIFF_NORMED)
        (min_x, max_y, minloc, maxloc) = cv.MinMaxLoc(result)
        (x,y) = minloc
        X1 = (x*1366)/640
        Y1 = (y*768)/480
        print X1, Y1
        #using pyautogui to move mouse
        pyautogui.moveTo(x+300, y)
        cv.Rectangle(frame, (x, y), (x+w, y+h), color, 1, 0)
        cv.NamedWindow("Image", 1)
        cv.MoveWindow("Image",300, 0)
        cv.ShowImage("Image", frame)

        if cv.WaitKey(10) == 27:
                   break

