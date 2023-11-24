import cv2 as cv
import mediapipe as mp

print('test')

# Initialise mediapipe objects
hands = mp.solutions.hands.Hands()
face = mp.solutions.face_mesh.FaceMesh()
face_detection = mp.solutions.face_detection.FaceDetection()  # Corrected module name
pose = mp.solutions.pose.Pose()

print(hands)
print(face)
print(face_detection)
print(pose)
