import cv2

caminho_imagem = 'teste.png'

# Carregar a imagem
imagem = cv2.imread(caminho_imagem)

# Aplicar o filtro da mediana com um kernel de 3x3
imagem_filtrada = cv2.medianBlur(imagem, 3)

# Mostrar a imagem original e a imagem filtrada
cv2.imshow('Imagem Original', imagem)
cv2.imshow('Imagem Filtrada (Filtro da Mediana)', imagem_filtrada)

# Esperar por uma tecla e fechar as janelas
cv2.waitKey(0)
cv2.destroyAllWindows()
