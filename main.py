from functions import *
from constants_and_ascii import *
from cowsay import tux


def game():
    no_error = True
    person_one = random_person()
    person_two = random_person()
    i=0
    while no_error == True:
        waiting(0)
        if i > 0:
            person_one = dict(person_two)
            person_two = random_person()
        print(logo)
        print('Quíen tiene más seguidores?')
        print(a_or_b[0])
        caracterisitcs(person_one)
        print(vs)
        print(a_or_b[1])
        caracterisitcs(person_two)
        guessing = input('Tiene más segidores... ').lower()
        person_higer = higer_lower(person_one['follower_count'],person_two['follower_count'])
        if guessing == person_higer:
            print('Correcto, vamos con el siguiente')
            i+=1
            waiting(5,clear_screen=False)
        elif guessing != person_higer:
            print('La respuesta es...')
            no_error = False
    waiting(5)
    print(GAME_OVER)
    print('''Incorrecto. Has perdido''')
    again = input('Quieres volver a jugar? (s/n) ').lower()
    return again



def main():
    try:
        introduction()
    except KeyboardInterrupt:
        pass
    waiting(0)
    jugar = 's'
    while jugar == 's':
        jugar = game()
    tux('Sabía que no eras tan bueno... No te creas amiga')
    waiting(5)
    tux('Gracias por jugar!!!')
    waiting(5)


if __name__ == '__main__':
    main()