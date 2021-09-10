###########################################
#####Importando los modulos necesarios#####
###########################################

from random import choice #
from constants_and_ascii import *
from getpass import getuser
from cowsay import tux
from time import sleep
from os import system


#######################################################
#####Definiendo funciones necesarias para el juego#####
#######################################################

def waiting(time,clear_screen=True):
    sleep(time)
    if clear_screen == True:
        system('clear')


def random_person(persons_used):
    datos = list(data)
    k = 0
    for i in datos:
        for j in persons_used:
            if j == i:
                datos.pop(k)
        k+=1
    return choice(datos)


def caracterisitcs(data):
    print(f'''Persona: {data['name']}
Breve descripción: {data['description']}
País: {data['country']}\n''')


def higer_lower(follower_one,follower_two):
    if follower_one > follower_two:
        return 'a'
    elif follower_two > follower_one:
        return 'b'


def tutorial():
    waiting(0)
    tux('Jugar Higer or Lower es bastante sencillo.')
    waiting(5)
    tux('En la pantalla te aparecerán dos cosas.')
    waiting(5)
    tux('Pueden ser personas, empresas, canales de televisión, etc.')
    waiting(5)
    tux('El punto del juego es adivinar cual de esas dos cosas es más famosa que la otra.')
    waiting(5)
    tux('Y eso es todo. Ahora que ya sabes jugar, vamos a ello.')


def introduction():
    tux(f'Hola {getuser()}')
    waiting(5)
    tux('En esta ocación, vamos a jugar...')
    waiting(5)
    print(logo)
    waiting(5)
    tux('Antes de empezar, sabes como jugar?')
    print('''Si se jugar = s
No se jugar = n''')
    tuto = input('La verdad es que... ').lower()
    if tuto == 's':
        waiting(0)
        tux('Genial!!! entonces vamos a jugar')
    else:
        tutorial()