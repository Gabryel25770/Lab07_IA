import numpy as np
import cv2
import matplotlib.pyplot as plt

# Carregando a imagem
img = cv2.imread('./imagens/Satelite.jpeg')

# Convertendo espaço de cores
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img_hls = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)

# Plot imagens
imagens = [img_rgb, img_gray, img_hsv, img_hls]

# Tamanho da figura para as imagens
plt.figure(figsize=(10, 10))  # Tamanho da figura
for i in range(4):
    plt.subplot(2, 2, i + 1)
    plt.imshow(imagens[i] if i != 1 else imagens[i], 'gray')  # 'gray' para escala de cinza
    plt.xticks([]), plt.yticks([])

plt.show()

# Exibindo a última imagem (HLS) em um tamanho maior
plt.figure(figsize=(8, 8))  # Tamanho maior para a imagem HLS
plt.imshow(img_hls)  # Exibe a imagem HLS em cores
plt.title('Imagem HLS')
plt.axis('off')  # Remove os eixos
plt.show()
