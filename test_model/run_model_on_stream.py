import cv2

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

# Load a model imported from Tensorflow
print("LOADING MODEL...")
model = cv2.dnn.readNetFromTensorflow('exported_model_v3/frozen_inference_graph.pb', 'exported_model_v3/graph.pbtxt')
print("[MODEL LOADED]")

while True:
    success, image = cap.read()

    if image is not None:
        model.setInput(cv2.dnn.blobFromImage(image, size=(640, 640), swapRB=True))
        output = model.forward()

        output[0,0,:,:].shape is (100, 7)
        for detection in output[0, 0, :, :]:
            confidence = detection[2]
            if confidence > .85:
                print(str(detection[2])  + " shoe")
                image_height, image_width, _ = image.shape
                #resize box to fit on image
                box_x = detection[3] * image_width
                box_y = detection[4] * image_height
                box_width = detection[5] * image_width
                box_height = detection[6] * image_height
                #draw box
                cv2.rectangle(image, (int(box_x), int(box_y)), (int(box_width), int(box_height)), (255, 0, 0), thickness=3)

        cv2.imshow('image',image)
        cv2.waitKey(1)
