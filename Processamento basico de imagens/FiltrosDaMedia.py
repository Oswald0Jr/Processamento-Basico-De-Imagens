import cv2
import matplotlib.pyplot as plt

# Defina o caminho para a sua imagem
caminho_imagem = 'caminho/para/sua/imagem.jpg'

# Carregar a imagem
imagem = cv2.imread(caminho_imagem)

# Verificar se a imagem foi carregada corretamente
if imagem is None:
    print(f"Erro ao carregar a imagem em: {caminho_imagem}")
else:
    # Aplicar o filtro da média
    ksize = (5, 5)  # Tamanho do kernel
    imagem_filtro_media = cv2.blur(imagem, ksize)

    # Mostrar a imagem original e a imagem com o filtro da média
    plt.figure(figsize=(10, 5))

    # Imagem original
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB))
    plt.title('Imagem Original')
    plt.axis('off')

    # Imagem com filtro da média
    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(imagem_filtro_media, cv2.COLOR_BGR2RGB))
    plt.title('Imagem com Filtro da Média')
    plt.axis('off')

    plt.tight_layout()
    plt.show()
