def update_blink_count(ear, frame_counter, blink_count):
    EAR_THRESHOLD = 0.2
    CONSEC_FRAMES = 2

    if ear < EAR_THRESHOLD:
        frame_counter += 1
    else:
        if frame_counter >= CONSEC_FRAMES:
            blink_count += 1

        frame_counter = 0

    return frame_counter, blink_count