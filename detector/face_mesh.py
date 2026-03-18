import mediapipe as mp

class FaceMeshDetector:
    def __init__(self):
        self.face_mesh = mp.solutions.face_mesh.FaceMesh()

    def get_landmarks(self, frame_rgb):
        results = self.face_mesh.process(frame_rgb)

        if results.multi_face_landmarks:
            return results.multi_face_landmarks[0]
        else:
            return None