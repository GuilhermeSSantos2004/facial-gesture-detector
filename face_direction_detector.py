import cv2
import mediapipe as mp
import serial
import time

# Inicia comunicação serial com o Arduino
arduino = serial.Serial('COM6', 9600, timeout=1)
time.sleep(2)

# Inicializa Mediapipe Pose e Face Mesh
mp_pose = mp.solutions.pose
mp_face = mp.solutions.face_mesh
pose = mp_pose.Pose()
face_mesh = mp_face.FaceMesh()

cap = cv2.VideoCapture('video01.mp4')

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Processamento do corpo
    pose_results = pose.process(rgb_frame)

    

    if pose_results.pose_landmarks:
        landmarks = pose_results.pose_landmarks.landmark
        head_y = landmarks[0].y

        right_hand_y = landmarks[16].y
        left_hand_y = landmarks[15].y

        # LED Vermelho (mão direita acima da cabeça)
        if right_hand_y < head_y:
            arduino.write(b'R')
        else:
            arduino.write(b'r')

        # LED Verde (mão esquerda acima da cabeça)
        if left_hand_y < head_y:
            arduino.write(b'G')
        else:
            arduino.write(b'g')

    # Processamento facial
    face_results = face_mesh.process(rgb_frame)

    if face_results.multi_face_landmarks:
        face_landmarks = face_results.multi_face_landmarks[0].landmark

        # Olho direito (índices 159 e 145)
        right_eye_opening = abs(face_landmarks[159].y - face_landmarks[145].y)
        # Olho esquerdo (índices 386 e 374)
        left_eye_opening = abs(face_landmarks[386].y - face_landmarks[374].y)

        EYE_THRESHOLD = 0.0038

        print(right_eye_opening)

        # LED Azul (olho direito fechado)
        if right_eye_opening < EYE_THRESHOLD:
            arduino.write(b'B')
        else:
            arduino.write(b'b')

        # LED Amarelo (olho esquerdo fechado)
        if left_eye_opening < EYE_THRESHOLD:
            arduino.write(b'Y')
        else:
            arduino.write(b'y')

    cv2.imshow('CheckPoint 2 - Pose e Face', frame)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cap.release()
arduino.close()
cv2.destroyAllWindows()

