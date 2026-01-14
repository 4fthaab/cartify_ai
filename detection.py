import cv2

cap = cv2.VideoCapture(0)

print("Starting Cartify Detection (Mock Mode)...")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    h, w, _ = frame.shape

    # Fake detection box
    cv2.rectangle(
        frame,
        (int(w*0.3), int(h*0.3)),
        (int(w*0.7), int(h*0.7)),
        (0, 255, 0),
        2
    )

    cv2.putText(
        frame,
        "biscuit_good_day (0.92)",
        (int(w*0.3), int(h*0.28)),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 0),
        2
    )

    cv2.imshow("Cartify Smart Cart Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
