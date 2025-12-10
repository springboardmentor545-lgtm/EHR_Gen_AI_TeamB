import cv2
import numpy as np

def enhance_image_bytes(image_bytes):
    # Convert bytes → numpy array
    image_array = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

    # SIMPLE enhancement: sharpen filter (placeholder)
    kernel = np.array([[0, -1, 0],
                      [-1,  5, -1],
                      [0, -1, 0]])
    enhanced = cv2.filter2D(img, -1, kernel)

    _, enhanced_bytes = cv2.imencode(".jpg", enhanced)
    return enhanced_bytes.tobytes()
