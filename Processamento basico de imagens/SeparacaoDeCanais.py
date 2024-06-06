import cv2
import matplotlib.pyplot as plt

# Carregar a imagem
imagem = cv2.imread('teste.png')

# Separar os canais R, G e B
B, G, R = cv2.split(imagem)

# Mostrar a imagem original e os canais separados
plt.figure(figsize=(10, 7))

# Imagem original
plt.subplot(2, 2, 1)
plt.imshow(cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB))
plt.title('Imagem Original')
plt.axis('off')

# Canal R (vermelho)
plt.subplot(2, 2, 2)
plt.imshow(R, cmap='Reds')
plt.title('Canal Vermelho (R)')
plt.axis('off')

# Canal G (verde)
plt.subplot(2, 2, 3)
plt.imshow(G, cmap='Greens')
plt.title('Canal Verde (G)')
plt.axis('off')

# Canal B (azul)
plt.subplot(2, 2, 4)
plt.imshow(B, cmap='Blues')
plt.title('Canal Azul (B)')
plt.axis('off')

plt.tight_layout()
plt.show()
