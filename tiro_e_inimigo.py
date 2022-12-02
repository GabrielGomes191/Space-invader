from PPlay.sprite import *
from PPlay.collision import *
from random import randint
from pygame import mixer

janela_altura = 1280
janela_largura = 720

def atirar(nave, janela, teclado, vely, lista, cooldown):
    if teclado.key_pressed("SPACE") and cooldown == 0:
        criar_shoot(lista, nave)
        cooldown = 25
    if len(lista) > 0:
        for shoot in lista:
            shoot.draw()
            shoot.y -= 1000 * janela.delta_time()
            if shoot.y < -10:
                lista.remove(shoot)
    if cooldown > 0:
        cooldown -= 1
    return cooldown    

def criar_shoot(lista,nave):
    tiro = Sprite("assets\Tiro.png")
    tiro.x = nave.x + 22
    tiro.y = nave.y - 30
    lista.append(tiro)

def atirar_alien(matriz_inimigos, janela, lista_tirosalien, vely, nave, vidas, listas_vidas, invencibilidade, difirap):
    criar_shoot_alien(matriz_inimigos, lista_tirosalien, difirap)
    if len(lista_tirosalien) > 0:
        for tiro in lista_tirosalien:
            tiro.draw()
            tiro.y += 700 * janela.delta_time()
            if tiro.y > janela_altura:
                lista_tirosalien.remove(tiro)     
    for k,tiro in enumerate(lista_tirosalien):
        if tiro.collided(nave) and invencibilidade == 0:
            if tiro.collided_perfect(nave):
                lista_tirosalien.pop(k)
                vidas -= 1                                                     
                listas_vidas.pop(vidas-1) 
                invencibilidade = 120

    return vidas, invencibilidade

def criar_shoot_alien(matriz_inimigos, lista_tirosalien, difirap):
    for i in matriz_inimigos:
        for j in i:
            tiro = Sprite("assets\Tiro_alien.png")
            tiro.x = j.x 
            tiro.y = j.y
            a = randint(1,difirap)
            if a == 15 and len(lista_tirosalien) == 0:
                lista_tirosalien.append(tiro)                
    
def criainimigo(matriz_inimigos, num_matriz):
    if num_matriz == 0:
        for linha in range(2, -1, -1):  #Checa a matriz de baixo pra cima, otimizando o numero de vezes que ela é checada
            l = []
            for coluna in range(8):
                    inimigo = Sprite("assets\inimigo.png")
                    inimigo.x = (40 + inimigo.width)*(coluna)
                    inimigo.y = (160 - inimigo.height)*(linha)
                    l.append(inimigo)
            matriz_inimigos.append(l)
        num_matriz += 1
    return num_matriz

def desenhainimigo(matriz_inimigos,contador):
    criainimigo(matriz_inimigos,contador)
    for i in matriz_inimigos:
        for j in i:
            j.draw()

def inimigoandando(matriz_inimigos, janela, vel, bateu, nave, dificuldade):
    colide = False
    for i in matriz_inimigos:
        for j in i:
            j.x += dificuldade * vel * janela.delta_time()
            if (j.x >= janela.width - 70 or j.x <= 0):
                colide = True   
            if j.collided(nave) or j.y >= nave.y:
                bateu = True
    if colide == True:
        vel = vel*(-1) 
        for i in matriz_inimigos:
            for j in i:
                j.x += dificuldade * vel * janela.delta_time()
                j.y += 20
    return vel, bateu, colide

def monstromorre(matriz_inimigos, lista, score, vel, contador_mortes, janela):
    for i,lista_inimigos in enumerate(matriz_inimigos):
        for j,alien in enumerate(lista_inimigos):
            for k,tiro in enumerate(lista):
                if tiro.collided(alien):
                    if tiro.collided_perfect(alien):
                        lista.pop(k)
                        lista_inimigos.pop(j)
                        score += 50
                        vel *= 1.009
                        contador_mortes -= 1
    return score, vel, contador_mortes