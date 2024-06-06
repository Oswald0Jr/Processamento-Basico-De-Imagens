import cv2

caminho_imagem = 'teste.png'

# Carregar a imagem
imagem = cv2.imread(caminho_imagem)

# Inverter horizontalmente
imagem_invertida_horizontal = cv2.flip(imagem, 1)

# Inverter verticalmente
imagem_invertida_vertical = cv2.flip(imagem, 0)

# Mostrar a imagem original e as imagens invertidas
cv2.imshow('Imagem Original', imagem)
cv2.imshow('Imagem Invertida Horizontalmente', imagem_invertida_horizontal)
cv2.imshow('Imagem Invertida Verticalmente', imagem_invertida_vertical)

# Esperar por uma tecla e fechar as janelas
cv2.waitKey(0)
cv2.destroyAllWindows()
