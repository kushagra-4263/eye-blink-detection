def get_eye_landmarks(landmarks, frame_shape):
    height, width, _ = frame_shape
    LEFT_EYE = [33, 160, 158, 133, 153, 144]
    RIGHT_EYE = [362, 385, 387, 263, 373, 380]

    left_eye = []
    right_eye = []


    for idx in LEFT_EYE:
        x = int(landmarks.landmark[idx].x * width)
        y = int(landmarks.landmark[idx].y * height)

        left_eye.append((x, y))

    for idx in RIGHT_EYE:
        x = int(landmarks.landmark[idx].x * width)
        y = int(landmarks.landmark[idx].y * height)

        right_eye.append((x, y))
    
    return left_eye, right_eye