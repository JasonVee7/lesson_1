try:
    import cv2
    print("OpenCV is installed.")
    print("OpenCV version:", cv2.__version__)
except ImportError:
    print("OpenCV is not installed.")
