from PPlay.window import *
from PPlay.gameimage import *
from pygame import mixer
from PPlay.sprite import *
from PPlay.keyboard import *
from PPlay.animation import *


def settings2():

    #dimensões
    janela2_largura = 1280
    janela2_altura = 720

    #criando a janela22
    janela2 = Window(janela2_largura, janela2_altura)
    janela2.set_title("Settings")

    #pegando a entrada do usuário
    teclado = janela2.get_keyboard()
    click = janela2.get_mouse()

    #botao play
    easy = Sprite("assets/easy.png")
    easy.set_position(janela2.width/2 - easy.width +148, 100)

    #botao play
    normal = Sprite("assets/normal.png")
    normal.set_position(janela2.width/2 - normal.width +160, 200)

    #botao play
    hard = Sprite("assets/hard.png")
    hard.set_position(janela2.width/2 - hard.width +158, 300)

    difirap = 0
    dificuldade = 0

    while True:

        janela2.update()
        normal.draw()
        easy.draw()
        hard.draw() 

            #botao exit
        if click.is_over_object(easy) and click.is_button_pressed(True):
            dificuldade = 0.5
            difirap = 160
            break
            #botao exit
        elif click.is_over_object(normal) and click.is_button_pressed(True):
            dificuldade = 1
            difirap = 130
            break
            
            #botao exit
        elif click.is_over_object(hard) and click.is_button_pressed(True):
            dificuldade = 1.5
            difirap = 90
            break

    return dificuldade, difirap