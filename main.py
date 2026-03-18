import cv2
from detector.face_mesh import FaceMeshDetector
from utils.eye_landmarks import get_eye_landmarks
from utils.ear import calculate_ear
from utils.blink_logic import update_blink_count


def main():
    cap = cv2.VideoCapture(0)
    detector = FaceMeshDetector()

    blink_count = 0
    frame_counter = 0

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Failed to grab frame")
            break

        # Mirror view
        frame = cv2.flip(frame, 1)

        # Convert BGR → RGB
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Get face landmarks
        landmarks = detector.get_landmarks(rgb)

        if landmarks:
            # 🔹 Get eye landmarks
            left_eye, right_eye = get_eye_landmarks(landmarks, frame.shape)

            # 🔹 Calculate EAR
            left_ear = calculate_ear(left_eye)
            right_ear = calculate_ear(right_eye)
            ear = (left_ear + right_ear) / 2.0

            # 🔹 Update blink count
            frame_counter, blink_count = update_blink_count(
                ear, frame_counter, blink_count
            )

            # 🔹 UI PANEL (background)
            cv2.rectangle(frame, (10, 10), (320, 160), (0, 0, 0), -1)

            # 🔹 Title
            cv2.putText(frame, "BLINK COUNTER", (20, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)

            # 🔹 Blink count
            cv2.putText(frame, f"Blinks: {blink_count}", (20, 80),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

            # 🔹 Eye status
            status = "Eyes Closed" if ear < 0.2 else "Eyes Open"
            color = (0, 0, 255) if ear < 0.2 else (255, 255, 0)

            cv2.putText(frame, f"Status: {status}", (20, 120),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

        else:
            cv2.putText(frame, "No Face Detected", (20, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        # Show frame
        cv2.imshow("Blink Counter", frame)

        # Exit on ESC
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()