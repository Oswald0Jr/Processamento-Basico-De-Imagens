import cv2
import numpy as np
import matplotlib.pyplot as plt

# Defina o caminho para a sua imagem em tons de cinza
caminho_imagem = 'teste.png'

# Carregar a imagem em tons de cinza
imagem_cinza = cv2.imread(caminho_imagem, cv2.IMREAD_GRAYSCALE)

# Verificar se a imagem foi carregada corretamente
if imagem_cinza is None:
    print(f"Erro ao carregar a imagem em: {caminho_imagem}")
else:
    # Definir o valor de limiar para a binarização
    limiar = 128

    # Aplicar a limiarização manual
    _, imagem_binaria = cv2.threshold(imagem_cinza, limiar, 255, cv2.THRESH_BINARY)

    # Mostrar a imagem em tons de cinza e a imagem binarizada
    plt.figure(figsize=(10, 5))

    # Imagem em tons de cinza
    plt.subplot(1, 2, 1)
    plt.imshow(imagem_cinza, cmap='gray')
    plt.title('Imagem em Tons de Cinza')
    plt.axis('off')

    # Imagem binarizada (preto e branco)
    plt.subplot(1, 2, 2)
    plt.imshow(imagem_binaria, cmap='gray')
    plt.title('Imagem Preto e Branco')
    plt.axis('off')

    plt.tight_layout()
    plt.show()
