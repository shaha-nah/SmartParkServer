from flask import Flask, request, Response
import json
import numpy as np
import cv2
import os
import time

# Initialize the Flask application
app = Flask(__name__)


# route http posts to this method
@app.route('/api/carDetection', methods=['POST'])
def carDetection():
    r = request
    # convert string of image data to uint8
    nparr = np.fromstring(r.data, np.uint8)
    # decode image
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    #load COCO class labels
    labelsPath = os.path.sep.join(["./yolo-coco/", "coco.names"])
    LABELS = open(labelsPath).read().strip().split("\n")

    #derive paths to YOLO weights and model configuration
    weightsPath = os.path.sep.join(["./yolo-coco/", "yolov3.weights"])
    configPath = os.path.sep.join(["./yolo-coco/", "yolov3.cfg"])

    #load YOLO object detector
    net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)

    (H, W) = image.shape[:2]

    #determine output layer names
    ln = net.getLayerNames()
    ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]

    #obtain bounding box and associated probabilities
    blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)
    start = time.time()
    layerOutputs = net.forward(ln)
    end = time.time()

    #initialize confidence and class ID
    confidences = []
    classIDs = []

    #loop over layer outputs
    for output in layerOutputs:
        #loop over detection
        for detection in output:
            scores = detection[5:]
            classID = np.argmax(scores)
            confidence = scores[classID]

            #filter weak predictions
            if (confidence > 0.5):
                confidences.append(float(confidence))
                if (classID == 2):
                    classIDs.append(classID)
    
    if (len(classIDs) > 0):
        response = {"result": "car"}
    else:
        response = {"result": "none"}

    # encode response
    jsonResponse = json.dumps(response)

    return Response(response=jsonResponse, status=200, mimetype="application/json")


# start flask app
app.run(host="0.0.0.0", port=5000)