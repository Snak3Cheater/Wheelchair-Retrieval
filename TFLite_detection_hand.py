# Import packages
import os
import cv2
import numpy as np
import time
from threading import Thread
import importlib.util
import auto_drive as auto
import UltrasonicSensor as dist


# Webcam Settings -------------------------------------------------------------------------------------------------
class VideoStream:
    """Camera object that controls video streaming from the Picamera"""

    def __init__(self, resolution=(640, 480), framerate=30):
        # Initialize the PiCamera and the camera image stream
        self.stream = cv2.VideoCapture(0)
        ret = self.stream.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
        ret = self.stream.set(3, resolution[0])
        ret = self.stream.set(4, resolution[1])

        # Read first frame from the stream
        (self.grabbed, self.frame) = self.stream.read()

        # Variable to control when the camera is stopped
        self.stopped = False

    def start(self):
        # Start the thread that reads frames from the video stream
        Thread(target=self.update, args=()).start()
        return self

    def update(self):
        # Keep looping indefinitely until the thread is stopped
        while True:
            # If the camera is stopped, stop the thread
            if self.stopped:
                # Close camera resources
                self.stream.release()
                return

            # Otherwise, grab the next frame from the stream
            (self.grabbed, self.frame) = self.stream.read()

    def read(self):
        # Return the most recent frame
        return self.frame

    def stop(self):
        # Indicate that the camera and thread should be stopped
        self.stopped = True


def object_recognition():
    # MODEL SETTINGS -------------------------------------------------------------------------------------------------
    # Remember to change model paths when on Raspberry Pi
    MODEL_NAME = "/home/pi/Desktop/Handicap_Helper"
    GRAPH_NAME = 'detect_hand.tflite'  # DEFAULT NAME
    LABELMAP_NAME = 'labelmap3.txt'  # DEFAULT NAME
    min_conf_threshold = float(0.8)  # Confidence Threshold to SHOW
    resW, resH = 1280, 720
    imW, imH = int(resW), int(resH)

    # Importing Tensorflow Libraries --------------------------------------------------------------------------------
    pkg = importlib.util.find_spec('tflite_runtime')
    if pkg:
        from tflite_runtime.interpreter import Interpreter
    else:
        from tensorflow.lite.python.interpreter import Interpreter

    # Pathing to Directories ------------------------------------------------------------------------
    CWD_PATH = os.getcwd()  # Path to Current Working Directory
    PATH_TO_CKPT = os.path.join(CWD_PATH, MODEL_NAME, GRAPH_NAME)  # Path to .tflite file which contains model
    PATH_TO_LABELS = os.path.join(CWD_PATH, MODEL_NAME, LABELMAP_NAME)  # Path to labelmap

    # Loading Label Map ------------------------------------------------------------------------------------------
    with open(PATH_TO_LABELS, 'r') as f:
        labels = [line.strip() for line in f.readlines()]

    # BUG FIX FOR REMOVING ??? LABELS ----------------------------------------------------------------------------
    if labels[0] == '???':
        del (labels[0])

    # Load the Tensorflow Lite model -----------------------------------------------------------------------------
    interpreter = Interpreter(model_path=PATH_TO_CKPT)
    interpreter.allocate_tensors()

    # Get model details -----------------------------------------------------------------------------
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    height = input_details[0]['shape'][1]
    width = input_details[0]['shape'][2]

    floating_model = (input_details[0]['dtype'] == np.float32)

    input_mean = 127.5
    input_std = 127.5

    # Initialize frame rate calculation -----------------------------------------------------------------------------
    frame_rate_calc = 1
    freq = cv2.getTickFrequency()

    # Initialize video stream -----------------------------------------------------------------------------
    videostream = VideoStream(resolution=(imW, imH), framerate=30).start()
    time.sleep(1)

    # for frame1 in camera.capture_continuous(rawCapture, format="bgr",use_video_port=True):
    while True:

        # Start timer (for calculating frame rate)
        t1 = cv2.getTickCount()

        # Grab frame from video stream
        frame1 = videostream.read()

        # Acquire frame and resize to expected shape [1xHxWx3]
        frame = frame1.copy()
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_resized = cv2.resize(frame_rgb, (width, height))
        input_data = np.expand_dims(frame_resized, axis=0)

        # Normalize pixel values if using a floating model (i.e. if model is non-quantized)
        if floating_model:
            input_data = (np.float32(input_data) - input_mean) / input_std

        # Perform the actual detection by running the model with the image as input
        interpreter.set_tensor(input_details[0]['index'], input_data)
        interpreter.invoke()

        # Retrieve detection results
        boxes = interpreter.get_tensor(output_details[1]['index'])[0]  # 1 Bounding box coordinates of detected objects
        classes = interpreter.get_tensor(output_details[3]['index'])[0]  # 3 Class index of detected objects
        scores = interpreter.get_tensor(output_details[0]['index'])[0]  # 0 Confidence of detected objects
        # num = interpreter.get_tensor(output_details[3]['index'])[0]  #2 Total number of detected objects

        # Loop over all detections and draw detection box if confidence is above minimum threshold
        for i in range(len(scores)):
            if (scores[i] > min_conf_threshold) and (scores[i] <= 1.0):
                # Get bounding box coordinates and draw box
                # Interpreter can return coordinates that are outside of image dimensions,
                # need to force them to be within image using max() and min()
                ymin = int(max(1, (boxes[i][0] * imH)))
                xmin = int(max(1, (boxes[i][1] * imW)))
                ymax = int(min(imH, (boxes[i][2] * imH)))
                xmax = int(min(imW, (boxes[i][3] * imW)))

                cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), (10, 255, 0), 2)
                center = [int((xmin + xmax)/2), int((ymin + ymax)/2)]

                # Draw label
                object_name = labels[int(classes[i])]  # Look up object name from "labels" array using class index
                label = '%s: %d%%' % (object_name, int(scores[i] * 100))  # Example: 'person: 72%'
                labelSize, baseLine = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 2)  # Get font size
                label_ymin = max(ymin, labelSize[1] + 10)  # Make sure not to draw label too close to top of window
                cv2.rectangle(frame, (xmin, label_ymin - labelSize[1] - 10),
                              (xmin + labelSize[0], label_ymin + baseLine - 10), (255, 255, 255),
                              cv2.FILLED)  # Draw white box to put label text in
                cv2.putText(frame, label, (xmin, label_ymin - 7), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0),
                            2)  # Draw label text

                # Location of the Chair
                # print(center)
                if 540 < center[0] < 740:
                    print('CENTERED')
                    auto.init()
                    auto.forward(6)
                    auto.init()
                    distance = dist.front_sensing()
                    auto.init()
                    auto.stop(0.5)
                    print(distance)
                    if distance <= 40:
                        print("Done")
                        auto.stop(5)


        # Draw framerate in corner of frame
        cv2.putText(frame, 'FPS: {0:.2f}'.format(frame_rate_calc), (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2,
                    cv2.LINE_AA)

        # All the results have been drawn on the frame, so it's time to display it.
        cv2.imshow('Object detector', frame)


        # Calculate framerate
        t2 = cv2.getTickCount()
        time1 = (t2 - t1) / freq
        frame_rate_calc = 1 / time1


        # Press 'q' to quit
        if cv2.waitKey(1) == ord('q'):
            break



    # Clean up
    cv2.destroyAllWindows()
    videostream.stop()

