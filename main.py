#################################################
#####Importando todos los modulos necesarios#####
#################################################

from functions import * #Modulo con todas las funciónes a utilizar
from constants_and_ascii import * #Modulo con todas las constantes y el arte ascii
from cowsay import tux #Importando a tux :3


######################################
#####Definiendo función del juego#####
######################################

def game():
    #Para checar que aún no se ha equivocado
    no_error = True
    #Para ir guardando las personas que ya le han aparecido
    persons_used = []
    #Primera selección de personas aleatorias
    person_one = random_person(persons_used)
    person_two = random_person(persons_used)
    #Agregando estas personas a la lista de personas usadas
    persons_used.append(person_one)
    persons_used.append(person_two)
    #Contados para saber la racha y tomar en cuenta si pasa del primer intento
    i=0
    while no_error == True:
        waiting(0)
        #condicion para seleccionar otra persona
        if i > 0 and len(data) != len(persons_used):
            #Guardamos el valor en otro punto de la memoria para no igualar la respuesta
            person_one = dict(person_two)
            #Seleccionando otra persona
            person_two = random_person(persons_used)
            #Agregando esta misma persona a la lista de personas usadas
            persons_used.append(person_two)
        #Si la persona ya tiene la lista de personas repetidas a la lista de datos, entonces...
        elif len(data) == len(persons_used):
            #Damos un poco de suspenso... y terminamos el ciclo
            print('Te tengo que decir algo...')
            waiting(5)
            break
        #Imprimimos el logo del juego
        print(logo)
        print('Quíen tiene más seguidores?')
        print(a_or_b[0])
        #Imprimiendo las caracterísiticas del la personas
        caracterisitcs(person_one)
        print(vs)
        print(a_or_b[1])
        caracterisitcs(person_two)
        #Buscando quien tiene más seguidores
        person_higer = higer_lower(person_one['follower_count'],person_two['follower_count'])
        #Preguntandole al usuario quien creé que tiene más seguidores
        guessing = input('Tiene más segidores... ').lower()
        #Si el usuario le atina, entonces...
        if guessing == person_higer:
            #Le imprimimos que no se ha equivocado y continuamos
            print('Correcto, vamos con el siguiente')
            i+=1
            waiting(4,clear_screen=False)
        #Si no, entonces...
        elif guessing != person_higer:
            #Le damos un poco de suspenso y...
            print('La respuesta es...')
            #Cambiamos el valor de no_error a falso puesto que ya se ha equivocado
            no_error = False
    #Si el tamaño de lista de las personas usadas es diferentes ó no_error es igual a falso, entonces quiere decir que se ha equivocado
    if len(persons_used) != len(data) or no_error == False:
        #Esperamos un poco y...
        waiting(5)
        #Le decimos que ha perdido.
        print(GAME_OVER)
        print(f'''Incorrecto. Has perdido.
Llevabas una racha de {i} personas sin perder.''')
        #Le preguntamos si quiere volver a jugar
        again = input('Quieres volver a jugar? (s/n) ').lower()
        return again
    #Si no, entonces...
    elif len(persons_used) == len(data):
        #Le mostramos que ha ganado, puesto que ya le ha atinado a toda nuestra base de datos
        print(WIN)
        print('Has ganado!!!')
        print('Le has atinado correctamente a toda la base de datos que tenemos xD')
        #Y le preguntamos que si quiere volver a jugar
        again = input('Quieres volver a jugar? (s/n) ').lower()


###########################
#####Función principal#####
###########################

def main():
    #Para saltarnos la introducción
    try:
        introduction()
    except KeyboardInterrupt:
        pass
    waiting(0)
    #Variable por si quiere volver a jugar
    jugar = 's'
    while jugar == 's':
        jugar = game()
    #Cuando ya no quiera jugar, le damos las gracias al usuario por jugar :)
    tux('Gracias por jugar!!!')
    waiting(5)


#####################
#####Entry point#####
#####################

if __name__ == '__main__':
    main()