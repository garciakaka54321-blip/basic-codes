import pygame
from random import randint

pygame.init()


#janela
altura, largura = 635, 1240
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("MATE OS ALIENS!!")

#fps
Clock = pygame.time.Clock()

#Carregamento e inserção de Imagens na Janela.
bg = pygame.image.load("curso-python/pngwing.com.png")
nave_principal = pygame.image.load("curso-python/sprite_nave_pequena.png")
nave_inimiga = pygame.image.load("curso-python/nave_inimiga_pequena.png")
missil = pygame.image.load("curso-python/missil_pequeno.png")
missil = pygame.transform.scale(missil, (30, 30))

#player
pos_player_x = 585
pos_player_y = 500
vel_nave_player = 11

#inimigo
pos_inimigo_x = randint(50, largura - 100)
pos_inimigo_y = -50
vel_nave_inimigo = 6

#missil
tiro_alvo = False
pos_x_missil = pos_player_x
pos_y_missil = pos_player_y
vel_missil = 18

#pontuação
pontuacao = 0


def resetar_inimigo():
    global pos_inimigo_x, pos_inimigo_y
    pos_inimigo_y = -50
    pos_inimigo_x = randint(50, largura - 100)


def resetar_missil():
    global tiro_alvo, pos_x_missil, pos_y_missil
    tiro_alvo = False
    pos_x_missil = pos_player_x + (nave_principal.get_width() // 2) - 15
    pos_y_missil = pos_player_y


#colisão
def colisoes():
    global pontuacao, pos_inimigo_y,tiro_alvo, pos_x_missil, pos_y_missil

    #se o player colidir com a nave inimiga ou o inimigo passar da tela
    if player_rect.colliderect(inimigo_rect) or inimigo_rect.y > altura:
        pontuacao -= 1
        resetar_inimigo()
        print(f"pontuação:{pontuacao}")

    
    elif missil_rect.colliderect(inimigo_rect) and tiro_alvo:
        pontuacao += 1
        resetar_inimigo()
        resetar_missil()
        tiro_alvo = False
        print(f"pontos:{pontuacao}")



def resultado():
    if pontuacao < 0:
        print("Você perdeu! GAME OVER!")
    else:
        print("Você ganhou! PARABÉNS!")

#loop principal
loop = True
while loop:
    Clock.tick(60) #limita o FPS em 60 htz

    #1. Eventos (fechar janela)
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            loop = False

    #2. Comandos do teclado.
    comandos = pygame.key.get_pressed()

    #movimento do player
    if comandos[pygame.K_UP] and pos_player_y > 10:
        pos_player_y -= vel_nave_player

    if comandos [pygame.K_DOWN] and pos_player_y < 530:
        pos_player_y += vel_nave_player
  
    if comandos [pygame.K_LEFT] and pos_player_x > 10:
        pos_player_x -= vel_nave_player

    if comandos[pygame.K_RIGHT] and pos_player_x < 1130:
            pos_player_x += vel_nave_player

    if comandos[pygame.K_SPACE]and not tiro_alvo:
        tiro_alvo = True

    #3. lògica do míssil
    if tiro_alvo:
        pos_y_missil -= vel_missil
        #se sair da tela, volta para a nave
        if pos_y_missil < -30:
            resetar_missil()

    else:
        # enquanto não atira, acompanha a posição da nave
        resetar_missil()

    #4. movimento do inimigo
    pos_inimigo_y += vel_nave_inimigo

    #5. Atualização das caixas de colisão
    player_rect = nave_principal.get_rect(topleft=(pos_player_x, pos_player_y))
    inimigo_rect = nave_inimiga.get_rect(topleft=(pos_inimigo_x,pos_inimigo_y))
    missil_rect = missil.get_rect(topleft=(pos_x_missil, pos_y_missil))

    colisoes()

    #6. desenhar tudo na tela

    janela.blit(bg, (0, 0))
    janela.blit(nave_principal, (pos_player_x, pos_player_y))
    janela.blit(nave_inimiga, (pos_inimigo_x, pos_inimigo_y))
    janela.blit(missil, (pos_x_missil, pos_y_missil))

    pygame.display.update()

pygame.quit()
print("-=" * 20)
resultado()
print("-=" * 20)