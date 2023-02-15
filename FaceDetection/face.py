import cv2
import face_recognition

# Carrega a imagem do rosto para comparar
imagem_referencia = face_recognition.load_image_file("minha_foto.jpg")
face_referencia = face_recognition.face_encodings(imagem_referencia)[0]

# Inicializa a webcam
webcam = cv2.VideoCapture(0)

while True:
    # Captura um frame da webcam
    ret, frame = webcam.read()

    # Converte o frame para escala de cinza
    frame_cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detecta os rostos presentes no frame
    faces = face_cascade.detectMultiScale(
        frame_cinza, scaleFactor=1.1, minNeighbors=5)

    # Para cada rosto detectado, realiza o reconhecimento facial
    for (x, y, w, h) in faces:
        face_atual = frame[y:y+h, x:x+w]
        face_codificada = face_recognition.face_encodings(face_atual)[0]
        distancia = face_recognition.face_distance(
            [face_referencia], face_codificada)

        # Se a distância entre as faces for menor que 0.6, é considerado que é você
        if distancia < 0.6:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, "É você!", (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        else:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
            cv2.putText(frame, "Nao é você!", (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    # Mostra o frame na tela
    cv2.imshow("Webcam", frame)

    # Espera pela tecla 'q' para sair do loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera a webcam e fecha as janelas
webcam.release()
cv2.destroyAllWindows()
