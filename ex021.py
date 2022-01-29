import pygame
# para tocar musica
pygame.init() #para iniciar
pygame.mixer.music.load('ex021.mp3')#para carregar
pygame.mixer.music.play()#para tocar
pygame.event.wait() #esperar o evento terminar para encerrar o programa

