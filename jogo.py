from math import ceil
import pygame
from pygame import mixer
from PPlay import sprite
from PPlay.window import *
from pygame import mixer
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.keyboard import *
from PPlay.animation import *
from ctypes.wintypes import RGB
from tiro_e_inimigo import *
import menu

def main(dificuldade, difirap):

    #dimensões
    janela3_largura = 1280
    janela3_altura = 720

    bateu = False
    vely = 200
    vel = 250
    lista = []
    lista2 = []
    lista_tirosalien = []
    contador = 0
    cooldown = 0
    score = 0
    contador_mortes = 24
    vidas = 3

    #criando a janela
    janela3 = Window(janela3_largura, janela3_altura)
    janela3.set_title("Space Invaders")

    #pegando a entrada do usuário
    teclado = janela3.get_keyboard()

    janelaover = Window(janela3_largura, janela3_altura)
    teclado2 = janelaover.get_keyboard()
    janelaover.set_title("Game Over")
    background = Sprite("assets\gameover.png")

    #colocando um fundo ao jogo
    fundo_jogo = Sprite("assets\Background.jpg")

    #sprite da nave e tiro
    nave = Sprite("assets\Carro.png" ,1)
    nave.set_position(janela3_largura/2 - 30 , 620)

    piscada = Sprite("assets\piscada.png", 4)
    piscada.set_total_duration(1000)

    clock = pygame.time.Clock()

    vida1 = Sprite("assets\Vidas.png")
    vida2 = Sprite("assets\Vidas.png")
    vida3 = Sprite("assets\Vidas.png")

    lista_vidas = [vida1, vida2, vida3]

    lista_vidas[2].x = 30
    lista_vidas[2].y = 10

    lista_vidas[0].x = 110
    lista_vidas[0].y = 10

    lista_vidas[1].x = 190
    lista_vidas[1].y = 10

    mixer.init()
    mixer.music.load("assets\Decisive-battle.wav")
    mixer.music.set_volume(0.5)
    mixer.music.play(-1)

    tomei = False

    invencibilidade = 0

    while True:
        fundo_jogo.draw()
        clock.tick()
        fps = str(ceil(clock.get_fps()))      
        janela3.draw_text("FPS:", janela_largura / 2 - 280 , janela_altura/2, size=32, color=(0, 255, 220), font_name="Arial", bold=True, italic=False)
        janela3.draw_text(fps, janela_largura / 2 - 200 , janela_altura/2, size=32, color=(0, 255, 220), font_name="Arial", bold=True, italic=False)
        janela3.draw_text("Score: ", janela_largura / 2 , janela_altura/2, size=32, color=(0, 255, 220), font_name="Arial", bold=True, italic=False)
        janela3.draw_text(str(score), janela_largura / 2 + 120 , janela_altura/2, size=32, color=(0, 255, 220), font_name="Arial", bold=True, italic=False)

        if teclado.key_pressed("D") and nave.x <= 1190:
            nave.x += 300 *janela3.delta_time()
        if teclado.key_pressed("A") and nave.x >= 0:
            nave.x -= 300 *janela3.delta_time()

        if teclado.key_pressed("ESC"):
            janela3.close()

        cooldown = atirar(nave, janela3, teclado, vely, lista, cooldown)

        contador = desenhainimigo(lista2,contador)

        vel, bateu, colide = inimigoandando(lista2, janela3, vel, bateu, nave, dificuldade)

        score, vel, contador_mortes = monstromorre(lista2, lista, score, vel, contador_mortes, janela3)

        vidas, invencibilidade = atirar_alien(lista2, janela3, lista_tirosalien, vely, nave, vidas, lista_vidas, invencibilidade, difirap)

        print(difirap, dificuldade)

        if invencibilidade > 0:
            piscada.x = nave.x
            piscada.y = nave.y
            piscada.draw()
            piscada.update()
            invencibilidade -= 1
        else:
            nave.draw()

        for i in lista_vidas:
            i.draw()

        if contador_mortes == 0:
            contador_mortes = 24
            vel += vel * 1.02 * janela3.delta_time() 
            contador = 0

        if bateu or vidas == 0:
            name = input("Insert your name: ")
            #Pontuação
            ranking_r = open('ranking.txt', 'r')
            conteudo = ranking_r.readlines()
            conteudo.append(name + " - " + str(score) + ".")
            ranking_r.close() 
            ranking_w = open('ranking.txt', 'w')
            ranking_w.writelines(conteudo)
            ranking_w.close()
            while True:
                background.draw()
                if teclado2.key_pressed("ESC"):
                    menu.menu()
                janelaover.update()
        janela3.update()


