import cv2
import numpy as np
import pyttsx3

# Load the pre-trained emotion detection model
emotion_proto = 'deploy.prototxt.txt'
emotion_model = 'res10_300x300_ssd_iter_140000.caffemodel'
net = cv2.dnn.readNetFromCaffe(emotion_proto, emotion_model)

# Initialize the TTS engine
engine = pyttsx3.init()

# Emotions labels
emotions = ["Angry", "Disgust", "Fear", "Happy", "Sad", "Surprise", "Neutral"]

# Open a connection to the first webcam
cap = cv2.VideoCapture(0)

# Flag to track if your face has been detected
detected = False

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        break

    # Resize frame to improve performance
    frame_resized = cv2.resize(frame, (300, 300))
    height, width = frame_resized.shape[:2]

    # Prepare input image for emotion detection
    blob = cv2.dnn.blobFromImage(frame_resized, 1.0, (300, 300), (104.0, 177.0, 123.0))

    # Set input and perform inference with the emotion detection model
    net.setInput(blob)
    detections = net.forward()

    # Find the dominant emotion
    emotion_idx = np.argmax(detections[0, 0, :, 2])
    emotion_label = emotions[emotion_idx]

    # Draw emotion label on frame
    cv2.putText(frame_resized, f'Emotion: {emotion_label}', (10, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    # If emotion detected and not previously detected, speak emotion
    if not detected:
        engine.say(f"You look {emotion_label}")
        engine.runAndWait()
        detected = True

    # Display the resulting frame
    cv2.imshow('Facial Expression Detection', frame_resized)

    # Exit loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()
