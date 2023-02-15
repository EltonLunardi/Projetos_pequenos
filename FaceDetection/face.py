import cv2

# Carrega o classificador de faces
face_cascade = cv2.CascadeClassifier(
    'FaceDetection\haarcascade_frontalface_default.xml')

# Inicializa a webcam
cap = cv2.VideoCapture(0)

# Define o tamanho mínimo e máximo para detecção do rosto
min_size = (30, 30)
max_size = (200, 200)

while True:
    # Lê o frame da webcam
    ret, frame = cap.read()

    # Converte o frame para escala de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detecta as faces no frame
    faces = face_cascade.detectMultiScale(
        gray, 1.3, 5, minSize=min_size, maxSize=max_size)

    # Desenha um retângulo ao redor das faces detectadas
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Mostra o frame na tela
    cv2.imshow('Face Detection', frame)

    # Sai do loop quando a tecla 'q' é pressionada
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera a webcam e fecha a janela do vídeo
cap.release()
cv2.destroyAllWindows()
