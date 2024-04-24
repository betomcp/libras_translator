import cv2
import mediapipe as mp
import libra_translator_lib as lbtl

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

vs = cv2.VideoCapture(0)

while True:
    ret, frame = vs.read()
    if not ret:
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            points = []
            landmark_idx = -1
            for landmark in hand_landmarks.landmark:
                landmark_idx += 1
                x, y = int(landmark.x * frame.shape[1]), int(landmark.y * frame.shape[0])
                # cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)
                # cv2.putText(frame, str(landmark_idx), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1, cv2.LINE_AA)
                points.append([x, y, landmark_idx])
            
            # tradução dos pontos em letra
            letter = lbtl.translate(points)
            cv2.putText(frame, letter, 
                        (points[0][0] - 20, points[0][1] + 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 
                        2.5, 
                        (20, 255, 10), 
                        3, 
                        cv2.LINE_AA)


    cv2.imshow("Hand Tracking", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
vs.release()
