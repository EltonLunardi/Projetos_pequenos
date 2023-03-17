import cv2
import dlib
import numpy as np

# Inicializa o detector de rosto e o classificador
detector = dlib.get_frontal_face_detector()
sp = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
facerec = dlib.face_recognition_model_v1(
    'dlib_face_recognition_resnet_model_v1.dat')

# Carrega a imagem de cadastro de rosto
known_face_image = cv2.imread('known_face.jpg')
known_face = detector(known_face_image)[0]
known_face_descriptor = facerec.compute_face_descriptor(
    known_face_image, sp(known_face))

# Inicializa a webcam
cap = cv2.VideoCapture(0)

while True:
    # Lê a imagem da webcam
    ret, frame = cap.read()

    # Detecta rostos na imagem da webcam
    faces = detector(frame)

    for face in faces:
        # Extrai as características faciais da imagem do rosto
        landmarks = sp(frame, face)
        face_descriptor = facerec.compute_face_descriptor(frame, landmarks)

        # Compara as características faciais do rosto com as características do rosto cadastrado
        distance = np.linalg.norm(
            np.array(face_descriptor) - np.array(known_face_descriptor))

        # Desenha um retângulo ao redor do rosto na imagem da webcam
        x, y, w, h = face.left(), face.top(), face.width(), face.height()
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

        # Escreve o nome do rosto detectado e a distância em relação ao rosto cadastrado
        if distance < 0.6:
            cv2.putText(frame, "Rosto cadastrado", (x-10, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        else:
            cv2.putText(frame, "Rosto desconhecido", (x-10, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    # Exibe a imagem da webcam com os rostos detectados
    cv2.imshow('Webcam', frame)

    # Encerra o programa se a tecla 'q' for pressionada
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Fecha a janela da webcam e libera a webcam
cap.release()
cv2.destroyAllWindows()

'''
Explicação:

Primeiro, importamos as bibliotecas necessárias: cv2 para acessar a webcam e exibir imagens, dlib para detecção de rostos e extração de características faciais e numpy para operações matemáticas.

Em seguida, inicializamos o detector de rosto e o classificador usando os arquivos pré-treinados shape_predictor_68_face_landmarks.dat e `dlib_face_recognition_resnet_model_v1.dat`, respectivamente. Esses arquivos contêm os modelos de classificador de rosto pré-treinados para o Dlib.

Carregamos a imagem de cadastro de rosto que será usada como referência para comparação com os rostos detectados.

Inicializamos a webcam usando o método VideoCapture() da biblioteca cv2.

Iniciamos um loop infinito que captura continuamente imagens da webcam e realiza a detecção de rosto e reconhecimento de face.

Detectamos os rostos na imagem da webcam usando o detector de rosto do Dlib.

Extraímos as características faciais da imagem do rosto usando o modelo do classificador de rosto do Dlib.

Comparamos as características faciais do rosto detectado com as características do rosto cadastrado usando a distância Euclidiana entre os vetores de características faciais.

Desenhamos um retângulo ao redor do rosto detectado na imagem da webcam.

Escrevemos o nome do rosto detectado e a distância em relação ao rosto cadastrado na imagem da webcam.

Exibimos a imagem da webcam com os rostos detectados e as informações de reconhecimento.

Encerramos o loop e fechamos a janela da webcam e liberamos a webcam usando o método release() da biblioteca cv2 quando a tecla 'q' é pressionada.

Lembre-se de que, para usar este código, você precisa ter a biblioteca OpenCV e a biblioteca Dlib instaladas em seu ambiente Python, bem como os arquivos de modelo pré-treinados do Dlib para o detector de rosto e o classificador de rosto. Você também precisa ter uma imagem de referência de rosto cadastrada previamente que será usada como referência para comparação com os rostos detectados na webcam.
'''
