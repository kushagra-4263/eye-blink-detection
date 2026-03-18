import numpy as np

def calculate_ear(eye_points):
    eye = np.array(eye_points)

    v1 = np.linalg.norm(eye[1] - eye[5])
    v2 = np.linalg.norm(eye[2] - eye[4])

    h = np.linalg.norm(eye[0] - eye[3])

    ear = (v1 + v2) / (2.0 * h)

    return ear