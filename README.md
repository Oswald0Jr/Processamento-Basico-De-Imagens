# Repositório de Processamento de Imagens

## Descrição

Este repositório contém códigos para várias técnicas de processamento de imagens, como Conversão para preto e branco, Filtro da mediana, Filtro da média, Girar imagem, Inversão de imagem, Separação de canais e Tons de cinza


## Processamento de Imagem para Preto e Branco

Este código realiza a conversão de uma imagem em tons de cinza para uma imagem binarizada (preto e branco). Ele utiliza a biblioteca OpenCV para carregar a imagem e aplicar a limiarização. A imagem resultante é exibida utilizando a biblioteca Matplotlib.

O código funciona da seguinte maneira:

1. Define o caminho para a imagem em tons de cinza.
2. Carrega a imagem em tons de cinza usando a função `cv2.imread`.
3. Verifica se a imagem foi carregada corretamente.
4. Define um valor de limiar para a binarização.
5. Aplica a limiarização manual usando a função `cv2.threshold`.
6. Mostra a imagem em tons de cinza e a imagem binarizada usando a biblioteca Matplotlib.


## Filtro da Mediana

Este código aplica o filtro da mediana em uma imagem. O filtro da mediana é uma técnica de processamento de imagens que é usada para reduzir o ruído em uma imagem. Ele funciona substituindo cada pixel da imagem pelo valor mediano dos pixels na vizinhança desse pixel.

O código funciona da seguinte maneira:

1. Define o caminho para a imagem.
2. Carrega a imagem usando a função `cv2.imread`.
3. Aplica o filtro da mediana com um kernel de 3x3 usando a função `cv2.medianBlur`.
4. Mostra a imagem original e a imagem filtrada usando a função `cv2.imshow`.
5. Espera por uma tecla e fecha as janelas usando as funções `cv2.waitKey` e `cv2.destroyAllWindows`.


## Filtro da Média

Este código aplica o filtro da média em uma imagem. O filtro da média é uma técnica de processamento de imagens que é usada para reduzir o ruído em uma imagem. Ele funciona substituindo cada pixel da imagem pelo valor médio dos pixels na vizinhança desse pixel.

O código funciona da seguinte maneira:

1. Define o caminho para a imagem.
2. Carrega a imagem usando a função `cv2.imread`.
3. Verifica se a imagem foi carregada corretamente.
4. Aplica o filtro da média com um kernel de 5x5 usando a função `cv2.blur`.
5. Mostra a imagem original e a imagem com o filtro da média usando a biblioteca Matplotlib.


## Girar Imagem

Este código realiza a rotação de uma imagem em 90 graus no sentido horário. Ele utiliza a biblioteca OpenCV para carregar a imagem, realizar a rotação e exibir as imagens.

O código funciona da seguinte maneira:

1. Define o caminho para a imagem.
2. Carrega a imagem usando a função `cv2.imread`.
3. Obtém a altura e a largura da imagem.
4. Rotaciona a imagem 90 graus no sentido horário usando a função `cv2.rotate`.
5. Mostra a imagem original e a imagem girada usando a função `cv2.imshow`.
6. Espera por uma tecla e fecha as janelas usando as funções `cv2.waitKey` e `cv2.destroyAllWindows`.


## Inverter Imagem

Este código realiza a inversão de uma imagem tanto horizontalmente quanto verticalmente. Ele utiliza a biblioteca OpenCV para carregar a imagem, realizar as inversões e exibir as imagens.

O código funciona da seguinte maneira:

1. Define o caminho para a imagem.
2. Carrega a imagem usando a função `cv2.imread`.
3. Inverte a imagem horizontalmente usando a função `cv2.flip` com o parâmetro `1`.
4. Inverte a imagem verticalmente usando a função `cv2.flip` com o parâmetro `0`.
5. Mostra a imagem original e as imagens invertidas usando a função `cv2.imshow`.
6. Espera por uma tecla e fecha as janelas usando as funções `cv2.waitKey` e `cv2.destroyAllWindows`.


## Separação de Canais

Este código realiza a separação dos canais de cores (vermelho, verde e azul) de uma imagem. Ele utiliza a biblioteca OpenCV para carregar a imagem e separar os canais, e a biblioteca Matplotlib para exibir as imagens.

O código funciona da seguinte maneira:

1. Define o caminho para a imagem.
2. Carrega a imagem usando a função `cv2.imread`.
3. Separa os canais R, G e B usando a função `cv2.split`.
4. Mostra a imagem original e os canais separados usando a biblioteca Matplotlib.


## Conversão para Tons de Cinza

Este código realiza a conversão de uma imagem colorida para tons de cinza. Ele utiliza a biblioteca OpenCV para carregar a imagem e realizar a conversão, e a biblioteca Matplotlib para exibir as imagens.

O código funciona da seguinte maneira:

1. Define o caminho para a imagem.
2. Carrega a imagem colorida usando a função `cv2.imread`.
3. Converte a imagem colorida para tons de cinza usando a função `cv2.cvtColor`.
4. Mostra a imagem original e a imagem em tons de cinza usando a biblioteca Matplotlib.
