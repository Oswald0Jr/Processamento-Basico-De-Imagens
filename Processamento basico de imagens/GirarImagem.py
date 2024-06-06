import cv2

caminho_imagem = 'teste.png'

# Carregar a imagem
imagem = cv2.imread(caminho_imagem)

# Obter altura e largura da imagem
altura, largura = imagem.shape[:2]

# Rotacionar a imagem 90 graus no sentido horário
imagem_girada = cv2.rotate(imagem, cv2.ROTATE_90_CLOCKWISE)

# Mostrar a imagem original e a imagem girada
cv2.imshow('Imagem Original', imagem)
cv2.imshow('Imagem Girada 90 graus', imagem_girada)

# Esperar por uma tecla e fechar as janelas
cv2.waitKey(0)
cv2.destroyAllWindows()
