try:
    import cv2
    print("OpenCV is installed.")
    print("OpenCV version:", cv2.__version__)
    
except ImportError:
    install_opencv = input("OpenCV is not installed. Do you want to install it? (y/n): ").strip().lower()
    if install_opencv == 'y':
        import subprocess
        subprocess.call(['pip', 'install', 'opencv-python'])
        print("OpenCV has been successfully installed.")
    else:
        print("OpenCV was not installed.")
