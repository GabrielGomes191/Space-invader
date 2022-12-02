from pygame import mixer
from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.keyboard import *
from PPlay.animation import *
from settings import *
from jogo import main
import rank
from pygame import mixer


def menu():

    mixer.init()
    mixer.music.load("assets\A-cruel-angel-s-thesis-director-s-edit-version.wav")
    mixer.music.set_volume(0.5)
    mixer.music.play(-1)

    #dimensões
    janela_largura = 1280
    janela_altura = 720

    #criando a janela
    janela = Window(janela_largura, janela_altura)
    janela.set_title("Menu")

    #pegando a entrada do usuário
    click = janela.get_mouse()

    #titulo
    titulo = Sprite("assets\Titulo.png")
    titulo.set_position(janela.width/2 - 230 , -20)

    #fundo do menu
    background = Sprite("assets\menud.jpg")

    #botao play
    play = Sprite("assets\play.png")
    play.set_position(janela.width/2 - play.width +75, 350)

    #botao exit
    exit = Sprite("assets\exit.png")
    exit.set_position(janela.width/2 - play.width +75 , 450)

    #config
    config = Sprite("assets\settings.png")
    config.set_position(janela.width/2 - play.width +75 , 550)

    #rank
    ranki = Sprite("assets\Rank.png")
    ranki.set_position(70 , 600)

    dificuldade = 0.5
    difirap = 170

    while True:
        #desenhar tudo
        background.draw()
        titulo.draw()
        ranki.draw()
        config.draw()
        play.draw()
        exit.draw()

        #botao play
        if click.is_over_object(play) and click.is_button_pressed(True):
            main(dificuldade, difirap)            

        #botao exit
        elif click.is_over_object(exit) and click.is_button_pressed(True):
            janela.close()
        
        #botao settings
        elif click.is_over_object(config) and click.is_button_pressed(True):
            dificuldade, difirap = settings2()

        #botao rank
        elif click.is_over_object(ranki) and click.is_button_pressed(True):
            rank.rank()
        
        janela.update()