import cv2
import matplotlib.pyplot as plt

# Carregar a imagem colorida
imagem_colorida = cv2.imread('teste.png')

# Converter a imagem para tons de cinza
imagem_cinza = cv2.cvtColor(imagem_colorida, cv2.COLOR_BGR2GRAY)

# Mostrar a imagem original e a imagem em tons de cinza
plt.figure(figsize=(10, 5))

# Imagem original
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(imagem_colorida, cv2.COLOR_BGR2RGB))
plt.title('Imagem Colorida')
plt.axis('off')

# Imagem em tons de cinza
plt.subplot(1, 2, 2)
plt.imshow(imagem_cinza, cmap='gray')
plt.title('Imagem em Tons de Cinza')
plt.axis('off')

plt.tight_layout()
plt.show()
