# How to load a Tensorflow model using OpenCV
# Jean Vitor de Paulo Blog - https://jeanvitor.com/tensorflow-object-detecion-opencv/

import cv2
import math

def distance(p1,p2):
    return math.sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))

def find_closest(points):
    print(points)

    if not points:
        return "done"
    elif len(points)<=2:
        print("two")
        cv2.line(img, (int(points[0][0]),int(points[0][1])), (int(points[1][0]),int(centers[1][1])), (255, 255, 12), 9)
    else:
        best = [] #[dist,index]
        for p in range(1,len(points)):
            dist = distance(points[0],points[p])
            if not best:
                best.append(dist)
                best.append(p)
            #change best if this point is better
            else:
                if dist<best[0]:
                    best[0]=dist
                    best[1]=p
        #draw line
        cv2.line(img, (int(points[0][0]),int(points[0][1])), (int(points[p][0]),int(centers[p][1])), (36, 255, 12), 9)
        #remove two closest points
        points.pop(0)
        points.pop(best[1]-1)
        return find_closest(points)



# Load a model imported from Tensorflow
tensorflowNet = cv2.dnn.readNetFromTensorflow('exported_model_v3/frozen_inference_graph.pb', 'exported_model_v3/graph.pbtxt')
# Input image
img = cv2.imread('img.jpg')
rows, cols, channels = img.shape
# Use the given image as input, which needs to be blob(s).
tensorflowNet.setInput(cv2.dnn.blobFromImage(img, size=(640, 480), swapRB=True, crop=False))
# Runs a forward pass to compute the net output
networkOutput = tensorflowNet.forward()

centers = []
# Loop on the outputs
for detection in networkOutput[0,0]:
    score = float(detection[2])
    if score > 0.5:
    	#get points of box
        left = detection[3] * cols
        top = detection[4] * rows
        right = detection[5] * cols
        bottom = detection[6] * rows
        #find center of each box
        center = ((left+right)/2,(top+bottom)/2)
        centers.append(center)

        #draw a red rectangle around detected objects
        cv2.rectangle(img, (int(left), int(top)), (int(right), int(bottom)), (0, 0, 255), thickness=2)
        cv2.circle(img, (int(center[0]),int(center[1])), 5, (36, 255, 12), -1)

find_closest(centers)

# Show the image with a rectagle surrounding the detected objects 
cv2.imshow('Image', img)
cv2.waitKey()
cv2.destroyAllWindows()