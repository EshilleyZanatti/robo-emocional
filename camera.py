
import cv2
import mediapipe as mp
import serial
import time
import math

# ==========================================
# ARDUINO
# ==========================================

arduino = serial.Serial(
    "/dev/cu.usbserial-130",
    9600,
    timeout=1
)

time.sleep(2)

# ==========================================
# MEDIAPIPE
# ==========================================

mp_face_mesh = mp.solutions.face_mesh

face_mesh = mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

# ==========================================
# CÂMERA
# ==========================================

camera = cv2.VideoCapture(0)

emocao_atual = "NEUTRO"
candidata = "NEUTRO"
contador = 0

# ==========================================
# DISTÂNCIA ENTRE DOIS PONTOS
# ==========================================

def distancia(a, b):
    return math.sqrt(
        (a.x - b.x) ** 2 +
        (a.y - b.y) ** 2
    )

# ==========================================
# CLASSIFICAR EMOÇÃO
# ==========================================

def detectar_emocao(pontos):

    # --------------------------------------
    # BOCA
    # --------------------------------------

    canto_esq = pontos[61]
    canto_dir = pontos[291]

    labio_sup = pontos[13]
    labio_inf = pontos[14]

    largura_boca = distancia(canto_esq, canto_dir)

    abertura_boca = distancia(labio_sup, labio_inf)

    centro_cantos_y = (
        canto_esq.y + canto_dir.y
    ) / 2

    centro_labios_y = (
        labio_sup.y + labio_inf.y
    ) / 2

    # Positivo = cantos para cima = sorriso
    sorriso = (
        centro_labios_y - centro_cantos_y
    ) / max(largura_boca, 0.001)

    # Abertura proporcional da boca
    abertura = abertura_boca / max(
        largura_boca, 0.001
    )

    # --------------------------------------
    # SOBRANCELHAS
    # --------------------------------------

    sobrancelha_esq = pontos[107]
    sobrancelha_dir = pontos[336]

    olho_esq = pontos[159]
    olho_dir = pontos[386]

    distancia_brow_esq = abs(
        olho_esq.y - sobrancelha_esq.y
    )

    distancia_brow_dir = abs(
        olho_dir.y - sobrancelha_dir.y
    )

    distancia_brows = (
        distancia_brow_esq +
        distancia_brow_dir
    ) / 2

    # --------------------------------------
    # EXPRESSÕES
    # --------------------------------------

    # SURPRESO
    if abertura > 0.32:
        return "SURPRESO"

    # FELIZ
    if sorriso > 0.10:
        return "FELIZ"

    # TRISTE
    if sorriso < -0.08:
        return "TRISTE"

    # BRAVO
    if distancia_brows < 0.045:
        return "BRAVO"

    # NEUTRO
    return "NEUTRO"


# ==========================================
# LOOP
# ==========================================

print()
print("==============================")
print("       ROBO EMOCIONAL")
print("==============================")
print("Camera iniciada!")
print("Pressione ESC para sair.")
print()

while True:

    sucesso, frame = camera.read()

    if not sucesso:
        print("Erro ao acessar a camera.")
        break

    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2RGB
    )

    resultado = face_mesh.process(rgb)

    emocao_detectada = "NEUTRO"

    if resultado.multi_face_landmarks:

        rosto = resultado.multi_face_landmarks[0]
        pontos = rosto.landmark

        emocao_detectada = detectar_emocao(pontos)

        # ----------------------------------
        # ESTABILIZAR EMOÇÃO
        # ----------------------------------

        if emocao_detectada == candidata:

            contador += 1

        else:

            candidata = emocao_detectada
            contador = 0

        # Só muda depois de vários frames
        if contador >= 8 and candidata != emocao_atual:

            emocao_atual = candidata

            arduino.write(
                (emocao_atual + "\n").encode()
            )

            print("Emocao:", emocao_atual)

        # ----------------------------------
        # CAIXA DO ROSTO
        # ----------------------------------

        altura, largura, _ = frame.shape

        xs = [p.x for p in pontos]
        ys = [p.y for p in pontos]

        x1 = max(
            0,
            int(min(xs) * largura) - 20
        )

        y1 = max(
            0,
            int(min(ys) * altura) - 20
        )

        x2 = min(
            largura,
            int(max(xs) * largura) + 20
        )

        y2 = min(
            altura,
            int(max(ys) * altura) + 20
        )

        cv2.rectangle(
            frame,
            (x1, y1),
            (x2, y2),
            (0, 255, 0),
            2
        )

    # ======================================
    # TEXTO NA TELA
    # ======================================

    cv2.putText(
        frame,
        "EMOCAO: " + emocao_atual,
        (20, 45),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 255, 255),
        2
    )

    cv2.imshow(
        "ROBO EMOCIONAL",
        frame
    )

    tecla = cv2.waitKey(1) & 0xFF

    if tecla == 27:
        break


# ==========================================
# ENCERRAR
# ==========================================

camera.release()
cv2.destroyAllWindows()
face_mesh.close()
arduino.close()

print()
print("Robo encerrado.")
